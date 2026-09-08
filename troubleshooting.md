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
- Fix: 
- Retest evidence: 
- Related commit:
- Remaining uncertainty: