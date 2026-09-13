<img src="assets/barq-logo.svg" alt="BARQ Systems" width="180">

# BARQ Academy DevOps Internship - Production Environment

A production-ready, highly available, multi-container REST API infrastructure running three replicated Flask application instances behind an NGINX reverse proxy on port 8090, backed by PostgreSQL 16 and Redis 7.4.

---

## 1. System Architecture Overview

- **Public Ingress**: Host port `8090` forwards traffic to NGINX (container: `nginx`, listening on port 80).
- **Application Tier**: 3 Flask API replicas (`app-01`, `app-02`, `app-03`) running Gunicorn on port 8080 under a dedicated non-root user `app` (UID `10001`).
- **Persistence & Caching Tier**:
  - **PostgreSQL 16**: Internal port 5432 with persistent named volume `postgres-data`.
  - **Redis 7.4**: Internal port 6379 with Append-Only File (AOF) persistence and named volume `redis-data`.
- **Network Segmentation**:
  - `frontend` network: Bridges `nginx` with `app-01`, `app-02`, and `app-03`.
  - `backend` network (`internal: true`): Bridges `app-01`, `app-02`, `app-03` with `postgres` and `redis`.
  - *Direct network communication between NGINX and PostgreSQL/Redis is strictly blocked.*
- **Visual Diagram**: Refer to [`architecture.png`](docs/Architecture.png) for detailed request flows, ports, volumes, and health relationships.

---

## 2. API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Service identity and welcome message |
| `/health` | `GET` | Application process liveness probe |
| `/ready` | `GET` | Deep dependency probe (validates PostgreSQL and Redis readiness) |
| `/instance` | `GET` | Returns upstream backend identifier (`app-01`, `app-02`, or `app-03`) |
| `/records` | `GET`, `POST` | Lists and inserts persistent records in PostgreSQL |
| `/counter` | `GET` | Atomically increments and returns Redis-backed visit count |

---

## 3. Copyable Commands

### Prerequisites
- Linux or WSL2
- Docker Engine & Docker Compose v2
- Python 3.12 with `pip`

### Step A: Setup & Configuration
```bash
# 1. Create your local environment configuration
cp .env.example .env

# 2. (Optional) Setup Python virtual environment for local tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt requests
```

### Step B: Build & Start Services
```bash
# Build images and launch all containers in background
docker compose up --build -d

# Verify all services are up and healthy
docker compose ps
```

### Step C: Verification & Testing
```bash
# 1. Run app-only unit tests (mocked dependencies)
python -m unittest discover -s tests -v

# 2. Run end-to-end integration validation against running containers
python validate.py
```

### Step D: Failure & Availability Testing
```bash
# Verify traffic continues serving when one backend is stopped, then recovered
python failure_test.py
```

### Step E: Database Backup & Restore Verification
```bash
# 1. Take a PostgreSQL backup
bash backup.sh

# 2. Restore PostgreSQL records from backup file
bash restore.sh
```

### Step F: Video Challenge Script
```bash
# Run during the continuous recording after repairing the environment
./video_challenge.sh
```

### Step G: Teardown & Cleanup
```bash
# Stop all containers safely without removing persistent volumes
docker compose down

# Full cleanup (WARNING: removes persistent database & redis volumes)
docker compose down -v
```

---

## 4. Documentation Index

- [`troubleshooting.md`](troubleshooting.md): Chronological engineering journal recording symptoms, root causes, fixes, and retests.
- [`log_analysis.md`](log_analysis.md): Correlated investigation of `access.log`, `error.log`, and `application.log`.
- [`decisions.md`](decisions.md): 5 core architectural decisions with alternatives, trade-offs, and production improvements.
- [`security_review.md`](security_review.md): Review of 8 concrete security risks and production follow-ups.
- [`trivy_images_scan_report.md`](trivy_images_scan_report.md): **(Bonus Task / Extra Credit)** A Trivy vulnerability scan report across all stack images (`app`, `nginx`, `postgres`, `redis`).
- [`docs/EVIDENCE_INDEX.md`](docs/EVIDENCE_INDEX.md): Master matrix linking assessment requirements to files, commits, and video timestamps.
- [`AI_USAGE.md`](AI_USAGE.md): Complete disclosure of AI tools and verification procedures.

---

### Bonus Task: Automated Image Security Scanning (Extra Credit)
As rewarded in [TASK.md](assessment/TASK.md#L51) (*"Extra credit (optional): add and document an image/security scan"*), automated vulnerability scanning is built directly into our GitHub Actions CI pipeline ([`.github/workflows/CI.yml`](.github/workflows/CI.yml)) using **Aqua Security Trivy**. It inspects both base OS packages and application dependencies across all container images:
- `barq-assessment-app-01` (Debian 12 slim + Python pip dependencies)
- `nginx:1.28-alpine`
- `postgres:16-alpine`
- `redis:7.4-alpine`

Complete scan outputs, CVE classifications, and severity breakdowns are compiled in [`trivy_images_scan_report.md`](trivy_images_scan_report.md).

---

## Technical Questions & Answers

### 1. What failed first? What proved the cause? Which failed attempt taught you something?
- **What failed first**: When I started from the baseline (`c8d8f15`) and ran `docker compose up`, the environment didn't work. The app containers failed health checks with 404, NGINX was resetting connections because of port 81, and `APP_HOST` was overriding `0.0.0.0` with `127.0.0.1` so NGINX couldn't reach the Flask apps.
- **What proved the cause**: 
  - I checked `docker compose logs` and saw the health check was requesting `/healthz` instead of `/health` (`89d8a6b`).
  - Checking `docker-compose.yml` showed NGINX mapped host port to container port 81 instead of 80 (`10d0e4d`).
  - Removing `APP_HOST` let Gunicorn bind properly to `0.0.0.0:8080` (`fce3aa2`).
  - Postgres logs showed database connection and password errors from `config/app.env` (`e67b527`).
- **Failed attempt that taught me something**: 
  - When testing NGINX failover, stopping one app gave a `504 Gateway Timeout` instead of switching to the healthy one. I investigated `nginx.conf` and found `proxy_next_upstream off;`. Deleting that line enabled immediate failover (`c149647`).
  - In CI, putting a dummy password in `.env.example` broke Postgres authentication because Compose defaults (`${VAR:-DEFAULT}`) only kick in when a variable is completely empty, teaching me how Compose variable substitution works (`a8b5a06`).

---

### 2. What patterns did the logs reveal? How did you avoid double-counting requests?
- **Patterns in the logs**: Looking at `access.log`, `error.log`, and `application.log`, I noticed a clear chain reaction: whenever backend Flask instances crashed, NGINX immediately logged 502 Bad Gateway and 504 Gateway Timeout errors. In the app log, database connection pool timeouts showed up right before the HTTP 503 errors on `/records` (`d8693fb`).
- **How I avoided double-counting**: NGINX generates a unique `request_id` for every request and passes it to Flask in the `X-Request-ID` header. When requests fail and get retried by the proxy, they can show up multiple times in the logs. So instead of just counting total log lines, I grouped the logs by unique `request_id` to get the true request count (`d8693fb`).

---

### 3. How do requests flow? Why these ports, networks and readiness checks?
- **Request flow**: 
  1. Client sends request to host port `8080` (or `8090` after the video challenge).
  2. NGINX receives it on port 80 (on the `frontend` network) and balances it round-robin between `app-01`, `app-02`, and `app-03` on internal port 8080 (`263e380`).
  3. The app instance talks to PostgreSQL (`5432`) and Redis (`6379`) over the isolated `backend` network.
  4. Response goes back through NGINX to the client with `X-Instance-ID`.
- **Why these ports & networks**: We only expose port `8080`/`8090` on the host through NGINX. We removed the host ports for Postgres (`15432`) and Redis (`16379`) so nobody can talk to the database directly from outside (`ce03ace`). We also took NGINX off the `backend` network so NGINX physically cannot reach Postgres or Redis directly (`cfef474`).
- **Why these readiness checks**: `/health` checks if the Flask process itself is alive, while `/ready` actually tests if Postgres and Redis connections can execute queries before sending real user traffic to the app.

---

### 4. Why these timeouts, retries, restart settings and resource limits?
- **Timeouts (2–5s)**: Set so if an app instance hangs, NGINX fails fast and redirects to another instance instead of freezing the client connection (`c149647`).
- **Retries (3–10)**: Postgres has `retries: 10` so it has enough time to initialize `init.sql` on startup before the app marks it as failed.
- **Restart policy (`restart: always`)**: Added to `docker-compose.yml` so that when an instance gets killed during `failure_test.py`, Docker automatically restarts it without manual intervention (`ed4bd8e`).
- **Resource limits**: Documented in `decisions.md` to keep memory and CPU usage bounded so one leaking container can't crash the whole host (`1bd66a0`).

---

### 5. When should validation fail? What does green CI prove, or not prove?
- **When validation fails**: If any core endpoint returns an error, if Postgres/Redis are down, if internal ports are exposed on the host, if NGINX reaches the backend network, or if round-robin stops working (`e0bd90c`).
- **What green CI proves**: The code passes unit tests, Compose syntax is valid, images pass Trivy vulnerability scans, containers spin up properly, and all `validate.py` checks pass on a clean Ubuntu runner (`ce3e6fe`).
- **What green CI does not prove**: It doesn't prove how the app handles thousands of simultaneous users, or how it behaves across multiple real cloud regions with network lag.

---

### 6. Which single points of failure (SPOFs) remain? How would you fix them in production?
- **Remaining SPOFs**:
  1. **Single NGINX container**: If NGINX goes down, all traffic stops.
  2. **Single Postgres container**: If the DB container or its storage volume corrupts, data writes fail (`29af7a4`).
  3. **Single Redis container**: If Redis stops, counter/cache operations fail (`d33060e`).
  4. **Single Host Machine**: Everything is running on one single Docker host (`3a24c7b`).
- **How I would fix them in production**:
  - Use a cloud load balancer (like AWS ALB) across multiple Availability Zones instead of one NGINX container.
  - Use a managed database like AWS RDS Multi-AZ or Postgres with Patroni for automatic failover.
  - Use Redis Sentinel or Redis Cluster for replication.
  - Run the containers in a Kubernetes cluster across multiple worker nodes with autoscaling (HPA) (`1bd66a0`).

---

### 7. What would you improve? How did you verify AI-assisted work?
- **What I would improve**:
  - Add HTTPS with Let's Encrypt certificates.
  - Add rate limiting in NGINX (`limit_req_zone`) to stop DDoS/brute-force attacks.
  - Add Prometheus and Grafana for live monitoring and alerts.
  - Use a real secrets manager (like HashiCorp Vault or AWS Secrets Manager) instead of `.env` files (`94b8a59`).
- **How I verified AI-assisted work**:
  - I didn't take suggestions blindly; I checked official Docker, NGINX, and Postgres docs.
  - I verified the non-root user fix directly in the container using `docker compose exec app-01 whoami` and `id` (`88a65a3`).
  - I verified everything with automated tests: `python -m unittest`, `validate.py`, `failure_test.py` (`33570d1`), and testing backup/restore with `backup.sh` and `restore.sh` (`a17088b`).