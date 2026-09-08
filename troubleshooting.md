# Troubleshooting journal


## Entry 01 / 2026-09-09 / 12:31 AM
- Symptom: When building the docker-compose.yml app-01 and app-02 had a 404 error when requesting /healthz
- Hypothesis: it didn't found an api with this name
- Command or test: `docker compose -p barq-assessment up --build -d`
- Actual output: `app-01    | 127.0.0.1 - - [08/Sep/2026 21:24:34] "GET /healthz HTTP/1.1" 404 -
 app-02    | {"timestamp": "2026-09-08T21:24:39.045+00:00", "level": "WARN", "service": "barq-api", "event": "http_request", "instance_id": "app-01", "request_id": "e2a936c5dd23444a9a400e7d2a378f35", "method": "GET", "path": "/healthz", "status": 404, "duration_ms": 0.183}
app-02    | 127.0.0.1 - - [08/Sep/2026 21:24:39] "GET /healthz HTTP/1.1" 404 - `
- Failed attempt and what changed your thinking: None
- Root cause: A syntax error in docker-compose.yml when configuring the health check the developer typed /healthz instead of /health
- Fix: changed the path in docker compose in `&app` from `/healthz` to `health`
- Retest evidence: When building the docker-compose file again it shows 200 ok in both app-01,02 ... `app-01    | {"timestamp": "2026-09-08T21:50:25.632+00:00", "level": "INFO", "service": "barq-api", "event": "http_request", "instance_id": "app-01", "request_id": "5d34ee4d1ac043ad8d970efec2926038", "method": "GET", "path": "/health", "status": 200, "duration_ms": 0.149}
app-01    | 127.0.0.1 - - [08/Sep/2026 21:50:25] "GET /health HTTP/1.1" 200 -
app-02    | {"timestamp": "2026-09-08T21:50:30.405+00:00", "level": "INFO", "service": "barq-api", "event": "http_request", "instance_id": "app-01", "request_id": "e5103f7524a54d40a0e825add45abf36", "method": "GET", "path": "/health", "status": 200, "duration_ms": 0.132}`
- Related commit:
- Remaining uncertainty: