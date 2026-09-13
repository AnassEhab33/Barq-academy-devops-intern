# Security and production-readiness review


Find 01:
- Risk and evidence: Postgres Database credentials POSTGRES_PASSWORD were hardcoded in plaintext inside docker-compose.yml
- Impact: Anyone with repository read access or access to image definitions can compromise the database
- Implemented fix / commit: 94b8a5909c60500ea213d80582f62d7fa9888e59
- Production follow-up: Use a secrets manager like AWS Secrets Manager or Kubernetes Secrets
- How to verify: git status --ignored verifies .env is ignored

Find 02:
- Risk and evidence: The Dockerfile was configured with USER root
- Impact: If the container is compromised, the attacker will have root access to the host
- Implemented fix / commit: 88a65a3449f3032066fd3fb13f15118450e2b92e
- Production follow-up: Use a non-root user with limited privileges
- How to verify: docker compose exec app-01 whoami returns app

Find 03:
- Risk and evidence: Unscanned Docker images may contain OS vulnerabilities.
- Impact: Known CVEs in base libraries could be leveraged for privilege escalation or remote code execution.
- Implemented fix / commit: Added automated Trivy vulnerability scanning in GitHub Actions CI.
- Production follow-up: Integrate continuous registry scanning like AWS ECR scanning
- How to verify: Review the Trivy scan output table in your GitHub Actions CI logs.

Find 04:
- Risk and evidence:Containers initially shared a flat network where NGINX could directly reach database ports.
- Impact: Compromising the public-facing NGINX reverse proxy would give an attacker direct network connectivity to the database.
- Implemented fix / commit: cfef474c5251455b1a504fd13d1faafa5227fa8e
- Production follow-up: implement zero-trust Kubernetes NetworkPolicies
- How to verify: docker compose exec nginx ping -c 1 postgres fails with name resolution or network unreachable.

Find 05:
- Risk and evidence: Lack of automated backup and restore validation risks permanent data loss on container recreation or volume corruption.
- Impact: loss of production data and downtime.
- Implemented fix / commit: a17088b8f14678c5d02f64f49f6d5f10136833fc
- Production follow-up: Automated snapshotting to cloud storage like AWS S3 with Point-In-Time Recovery
- How to verify: Run bash backup.sh followed by bash restore.sh and confirm /records preserves data.

Find 06:
- Risk and evidence: Unstructured or unredacted application logs could leak sensitive customer data or fail to record security events.
- Impact: Inability to investigate incidents, detect brute-force attacks, or comply with privacy regulations
- Implemented fix / commit: JSON structured logging in app/server.py with unique request_id, timestamps, and HTTP response codes.
- Production follow-up: Forward logs to a centralized, tamper-proof SIEM platform 
- How to verify: docker compose logs app-01 produces valid JSON structured log entries with request IDs.

Find 07:
- Risk and evidence: Single point of failure if an instance crashes or receives a traffic spike; lack of CPU/memory resource limits.
- Impact: A crash or memory leak in one instance takes down the whole service for all users.
- Implemented fix / commit: Deployed two replicated app backends (app-01 and app-02) behind NGINX round-robin load balancing, with container restart policies (restart: always) , ed4bd8e01b71f9951ef3ffe0ac7404afe5c77c57
- Production follow-up: Deploy across multiple availability zones in cloud providers
- How to verify: Run python failure_test.py to prove traffic continues serving seamlessly when one instance is stopped.

Find 08:
- Risk and evidence: In the starter docker-compose.yml, PostgreSQL (0.0.0.0:15432:5432) and Redis (0.0.0.0:16379:6379) were published directly to host interfaces.
- Impact: Anyone with access to the host network could bypass NGINX and connect directly to the PostgreSQL database or Redis 
- Implemented fix / commit: ce03ace63e59e5515d6eb912693c0e30e9cb2e6b
- How to verify: run nc -zv 127.0.0.1 15432 to confirm connection is refused.