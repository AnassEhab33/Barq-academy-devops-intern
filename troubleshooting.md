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
- Related commit: 89d8a6bd29e5921a19ffbfe90a82b9c7bb65f8c6
- Remaining uncertainty: No


## Entry 02 / 2026-09-09 / 1:10 AM
- Symptom: The app flags an error when trying curl on the localhost says Connection reset by peer
- Hypothesis: when i searched on this error i understood that it successfully reached something on `localhost:8080`, but the other side forcibly closed/reset the connection
- Command or test: `curl -v localhost:8080`
- Actual output: 
` connect to ::1 port 8080 from ::1 port 36906 failed: Connection refused 
  Trying 127.0.0.1:8080...
  Connected to localhost (127.0.0.1) port 8080
  Recv failure: Connection reset by peer
  Closing connection
  curl: (56) Recv failure: Connection reset by peer
`
- Failed attempt and what changed your thinking: No failed attempts
- Root cause: I found that when executing `docker ps` i found nginx ports was mapping when requesting the localhost:8080 to port 81 which no service running on this port so, thats why the connection was closed (`127.0.0.1:8080->81/tcp`)
- Fix: changed docker-compose.yml ports attribute from `127.0.0.1:${PUBLIC_PORT:-8080}:81` to `127.0.0.1:${PUBLIC_PORT:-8080}:80`
- Retest evidence: when i made curl localhost:8080 it showed me this output: `<html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
<hr><center>nginx/1.28.3</center>
</body>
</html>`

- Related commit: 10d0e4d46d991681cab52a0cf2bb99593547a726
- Remaining uncertainty: No


## Entry 03 / 2026-09-09 / 3:18 AM
- Symptom: Received a 503 status code when connecting to localhost:8080
- Hypothesis: I think it's a backend problem Maybe in the server itself. i will investigate in docker logs for nginx container
- Command or test: curl localhost:8080, docker logs nginx, docker exec -it app-01 sh, env | grep APP_
- Actual output: 

**For curl localhost:8080** <html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
<hr><center>nginx/1.28.3</center>
</body>
</html>

**For docker logs nginx:**
`{"timestamp":"2026-09-08T22:39:49+00:00","service":"edge","request_id":"1cee02083fb37fb680c919f3b2881aaa","method":"GET","path":"/","status":502,"upstream":"172.20.0.2:8081","upstream_status":"502","request_time":"0.001"}`

**For env | grep APP_ in app-01 container:** `APP_HOST=127.0.0.1
APP_MESSAGE=Welcome to BARQ Systems
APP_PORT=8080`


- **Failed attempt and what changed your thinking:** at the beginning i found in nginx.conf that the upstream in app-01 was sending requests in port 8081 and thought if i changed to 8080 i will solve the problem but, it still exists. so, i investigated more and more and found that the app-01,02 are listening on APP_HOST: "127.0.0.1" env variable which was overriden the implemented values in server.py (host=os.getenv("APP_HOST", "0.0.0.0")) by docker-compose environment.
- Root cause: Docker compose APP_HOST environment value overridden the implemented (host=os.getenv("APP_HOST", "0.0.0.0")) in the server.js which caused the app-01,02 containers to don't listen to any traffic unless it's from this overriden env that was configured in docker-compose (APP_HOST: "127.0.0.1")
- Fix: Removing the APP_HOST value leaving the actual value of the APP_HOST of the server.js
- Retest evidence: when i `curl localhost:8080` the output is now: `{"instance_id":"app-01","message":"Welcome to BARQ Systems","service":"barq-api","version":"2.0.0"}`
- Related commit: fce3aa2a1591f1e02f1c23abebfca4e872b79ca8
- Remaining uncertainty: No