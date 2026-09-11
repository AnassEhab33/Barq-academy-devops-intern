# Log analysis

Use all three supplied logs. Answer every question with commands/scripts and actual output.

1. What UTC interval is covered? How many valid, malformed and duplicate lines are in each file?
2. How many distinct client requests occurred? How did you deduplicate and avoid counting retries twice?
3. What are the final client status counts and error rate? State your denominator.
4. Which paths, time windows and backends account for the failures?
5. What are the median and p95 client latencies? State the percentile method and units.
6. Which requests retried upstream? How many succeeded after retrying?
7. Build an incident timeline using evidence from access, error AND application logs.
8. Show one correlated failed request and one successful request. Include IDs and timestamps.
9. Which errors appear to be proxy/connectivity issues versus dependency/application issues? What proves it?
10. What do the logs not prove? What would you check next in a running environment?

## Commands / scripts
### Q1: What UTC interval is covered? How many valid, malformed and duplicate lines are in each file?
```

# For interval in each log file 
grep -o '"timestamp":"[^"]*"' access.log | sort | sed -n '1p;$p'
"timestamp":"2026-08-20T11:00:00.015Z"
"timestamp":"2026-08-20T11:29:57.578Z"

grep -o '"timestamp": "[^"]*"' application.log | sort | sed -n '1p;$p'
"timestamp": "2026-08-20T11:00:00.015Z"
"timestamp": "2026-08-20T11:29:57.578Z"

awk '{print $1,$2}' error.log | sort | sed -n '1p;$p'
2026/08/20 11:05:02
2026/08/20 11:30:00

wc -l access.log error.log application.log
726 access.log
68 error.log
730 application.log

grep -c '^{.*}$' access.log
725
grep -c '^{.*}$' application.log
729


# For how many are malformed:
grep -vc '^{.*}$' access.log
1
grep -vc '^{.*}$' application.log
1

# what malformed records look like
grep -vn '^{.*}$' access.log
311:{"timestamp":"2026-08-20T11:12:48Z","request_id":

grep -vn '^{.*}$' access.log
311:{"timestamp":"2026-08-20T11:12:48Z","request_id":

# For duplicate lines in each file:
sort access.log | uniq -d
{"timestamp":"2026-08-20T11:05:00.055Z","request_id":"lab-000121","method":"GET","path":"/","status":200,"upstream":"172.23.0.11:8080","upstream_status":"200","request_time":0.055,"client":"192.0.2.24"}
{"timestamp":"2026-08-20T11:10:00.015Z","request_id":"lab-000241","method":"GET","path":"/","status":200,"upstream":"172.23.0.11:8080","upstream_status":"200","request_time":0.015,"client":"192.0.2.24"}
{"timestamp":"2026-08-20T11:15:00.055Z","request_id":"lab-000361","method":"GET","path":"/","status":200,"upstream":"172.23.0.11:8080","upstream_status":"200","request_time":0.055,"client":"192.0.2.24"}
{"timestamp":"2026-08-20T11:20:00.015Z","request_id":"lab-000481","method":"GET","path":"/","status":200,"upstream":"172.23.0.11:8080","upstream_status":"200","request_time":0.015,"client":"192.0.2.24"}
{"timestamp":"2026-08-20T11:25:00.055Z","request_id":"lab-000601","method":"GET","path":"/","status":200,"upstream":"172.23.0.11:8080","upstream_status":"200","request_time":0.055,"client":"192.0.2.24"}

sort application.log | uniq -d
{"timestamp": "2026-08-20T11:07:30.035Z", "level": "INFO", "event": "http_request", "request_id": "lab-000181", "instance_id": "app-01", "method": "GET", "path": "/", "status": 200, "duration_ms": 35.0}
{"timestamp": "2026-08-20T11:17:30.035Z", "level": "INFO", "event": "http_request", "request_id": "lab-000421", "instance_id": "app-01", "method": "GET", "path": "/", "status": 200, "duration_ms": 35.0}

sort error.log | uniq -d
empty
```

### Q2: How many distinct client requests occurred? How did you deduplicate and avoid counting retries twice?
```
# distinct request_ids in access.log
grep -o '"request_id":"[^"]*"' access.log | sort -u | wc -l
720

# find requests that internally retried to a second upstream
grep -c '"upstream":"[^"]*, ' access.log
19

```
### Q3: What are the final client status counts and error rate? State your denominator.
```
# for counting how many times each status code appears
sort -u access.log | grep -o '"status":[0-9]*' | sort | uniq -c
    615 "status":200
     10 "status":404
     40 "status":502
     47 "status":503
      8 "status":504

# counting the dominator (without duplicates)
sort -u access.log | grep -o '"status":[0-9]*' | wc -l
720
```
### Q4:

```
# for error 502 we will get it's affected paths, time windows and backends and so for each error
## having the paths affected with error 502:
sort -u access.log | grep '"status":502' | grep -o '"path":"[^"]*"' | sort | uniq -c
     10 "path":"/"
     10 "path":"/counter"
     10 "path":"/health"
     10 "path":"/records"

# seeing the time windows for this error
sort -u access.log | grep '"status":502' | grep -o '"timestamp":"[^"]*"' | sort | sed -n '1p;$p'
"timestamp":"2026-08-20T11:05:02.503Z"
"timestamp":"2026-08-20T11:09:57.503Z"

# seeing the number of logs for requested backends having 502 error
sort -u access.log | grep '"status":502' | grep -o '"upstream":"[^"]*"' | sort | uniq -c
     40 "upstream":"172.23.0.12:8080"

# For error 503:

sort -u access.log | grep '"status":503' | grep -o '"path":"[^"]*"' | sort | uniq -c
     16 "path":"/counter"
     23 "path":"/ready"
      8 "path":"/records"

sort -u access.log | grep '"status":503' | grep -o '"timestamp":"[^"]*"' | sort | sed -n '1p;$p'
"timestamp":"2026-08-20T11:12:09.525Z"
"timestamp":"2026-08-20T11:21:45.041Z"

sort -u access.log | grep '"status":503' | grep -o '"upstream":"[^"]*"' | sort | uniq -c
     23 "upstream":"172.23.0.11:8080"
     24 "upstream":"172.23.0.12:8080"

# For error 504:
sort -u access.log | grep '"status":504' | grep -o '"path":"[^"]*"' | sort | uniq -c
      8 "path":"/records"

sort -u access.log | grep '"status":504' | grep -o '"timestamp":"[^"]*"' | sort | sed -n '1p;$p'
"timestamp":"2026-08-20T11:25:14.501Z"
"timestamp":"2026-08-20T11:26:47.001Z"

sort -u access.log | grep '"status":504' | grep -o '"upstream":"[^"]*"' | sort | uniq -c
      4 "upstream":"172.23.0.11:8080"
      4 "upstream":"172.23.0.12:8080"

# what does error.log show during the 502 window?
awk '$0 >= "2026/08/20 11:05:02" && $0 <= "2026/08/20 11:09:57"' error.log | head -5
2026/08/20 11:05:02 [error] 31#31: *122 connect() failed (111: Connection refused) while connecting to upstream, request_id=lab-000122, request: "GET /health HTTP/1.1", upstream: "http://172.23.0.12:8080/health"
2026/08/20 11:05:07 [error] 31#31: *124 connect() failed (111: Connection refused) while connecting to upstream, request_id=lab-000124, request: "GET /ready HTTP/1.1", upstream: "http://172.23.0.12:8080/ready"
...

awk '$0 >= "2026/08/20 11:05:02" && $0 <= "2026/08/20 11:09:57"' error.log | wc -l
58

# what does error.log show during the 503 window?
awk '$0 >= "2026/08/20 11:12:09" && $0 <= "2026/08/20 11:21:45"' error.log | wc -l
0

# what does application.log show during the 503 window?
grep -c '"event": "dependency_error"' application.log
47

grep '"event": "dependency_error"' application.log | head -2
{"timestamp": "2026-08-20T11:12:09.524Z", "level": "ERROR", "event": "dependency_error", "request_id": "lab-000292", "instance_id": "app-02", "dependency": "redis", "error_type": "TimeoutError"}
{"timestamp": "2026-08-20T11:12:12.024Z", "level": "ERROR", "event": "dependency_error", "request_id": "lab-000293", "instance_id": "app-01", "dependency": "redis", "error_type": "TimeoutError"}

# what does error.log show during the 504 window?
awk '$0 >= "2026/08/20 11:25:14" && $0 <= "2026/08/20 11:26:47"' error.log
2026/08/20 11:25:14 [error] 31#31: *606 upstream timed out (110: Operation timed out) while reading response header from upstream, request_id=lab-000606, request: "GET /records HTTP/1.1", upstream: "http://172.23.0.12:8080/records"
2026/08/20 11:25:17 [error] 31#31: *607 upstream timed out (110: Operation timed out) while reading response header from upstream, request_id=lab-000607, request: "GET /records HTTP/1.1", upstream: "http://172.23.0.11:8080/records"
```

### Q5: What are the median and p95 client latencies? State the percentile method and units.

```
# pull the request_time value out of every line, sort numerically and put it in rt.txt
sort -u access.log | grep -o '"request_time":[0-9.]*' | sed 's/.*://' | sort -n > rt.txt

# how many values total
wc -l < rt.txt
720

# median = the value at rank 50% of n (720 * 0.50 = rank 360) so we will get the line 360 value
sed -n '360p' rt.txt
0.054

# p95 = the value at rank 95% of n (720 * 0.95 = rank 684) so we will get the line 684 value
sed -n '684p' rt.txt
2.001
```

### Q6: Which requests retried upstream? How many succeeded after retrying?
```
# for showing the upstream records that have two backends were requested for the same request (usally they have comma in there "upstream" field)
sort -u access.log | grep -c '"upstream":"[^"]*, '
19

# which request_ids retried
sort -u access.log | grep '"upstream":"[^"]*, ' | grep -o '"request_id":"[^"]*"'
"request_id":"lab-000124"
"request_id":"lab-000130"
"request_id":"lab-000136"
"request_id":"lab-000142"
"request_id":"lab-000148"
"request_id":"lab-000154"
"request_id":"lab-000160"
"request_id":"lab-000166"
"request_id":"lab-000172"
"request_id":"lab-000178"
"request_id":"lab-000184"
"request_id":"lab-000190"
"request_id":"lab-000196"
"request_id":"lab-000202"
"request_id":"lab-000208"
"request_id":"lab-000214"
"request_id":"lab-000220"
"request_id":"lab-000226"
"request_id":"lab-000232"

# their final status (if they succeeded or not)
sort -u access.log | grep '"upstream":"[^"]*, ' | grep -o '"status":[0-9]*' | sort | uniq -c
     19 "status":200

# which paths retried
sort -u access.log | grep '"upstream":"[^"]*, ' | grep -o '"path":"[^"]*"' | sort | uniq -c
      9 "path":"/instance"
     10 "path":"/ready"
```
### Q7: Build an incident timeline using evidence from access, error AND application logs.

```
# anchor points: first/last connect-refused error
grep "Connection refused" error.log | head -1
2026/08/20 11:05:02 [error] 31#31: *122 connect() failed (111: Connection refused) ... request_id=lab-000122 ... upstream: "http://172.23.0.12:8080/health"
grep "Connection refused" error.log | tail -1
2026/08/20 11:09:57 [error] 31#31: *240 connect() failed (111: Connection refused) ... request_id=lab-000240 ... upstream: "http://172.23.0.12:8080/"

# first successful retry during the outage
grep '"request_id":"lab-000124"' access.log
{"timestamp":"2026-08-20T11:05:07.620Z","request_id":"lab-000124",...,"status":200,"upstream":"172.23.0.12:8080, 172.23.0.11:8080","upstream_status":"502, 200",...}

# redis timeout window
grep '"dependency": "redis"' application.log | grep -o '"timestamp": "[^"]*"' | sort | sed -n '1p;$p'
"timestamp": "2026-08-20T11:12:09.524Z"
"timestamp": "2026-08-20T11:15:52.024Z"
grep -c '"dependency": "redis"' application.log
31

# postgres error window
grep '"dependency": "postgres"' application.log | grep -o '"timestamp": "[^"]*"' | sort | sed -n '1p;$p'
"timestamp": "2026-08-20T11:20:07.540Z"
"timestamp": "2026-08-20T11:21:45.040Z"
grep -c '"dependency": "postgres"' application.log
16

# upstream timeout window
grep "timed out" error.log | head -1
2026/08/20 11:25:14 [error] 31#31: *606 upstream timed out ... request_id=lab-000606 ... upstream: "http://172.23.0.12:8080/records"
grep "timed out" error.log | tail -1
2026/08/20 11:26:47 [error] 31#31: *643 upstream timed out ... request_id=lab-000643 ... upstream: "http://172.23.0.11:8080/records"

# end of the collection window
tail -1 access.log
{"timestamp":"2026-08-20T11:29:57.578Z","request_id":"lab-000720",...,"status":200,...}
grep "notice" error.log
2026/08/20 11:30:00 [notice] 31#31: log collector rotated stream
```
### Q8: 8. Show one correlated failed request and one successful request. Include IDs and timestamps.

```
# find a the first failed request_id in error.log
grep "Connection refused" error.log | head -1
2026/08/20 11:05:02 [error] 31#31: *122 connect() failed (111: Connection refused) while connecting to upstream, request_id=lab-000122, request: "GET /health HTTP/1.1", upstream: "http://172.23.0.12:8080/health"


# find a the first successful request_id in access.log
grep '"status":200' access.log | head -1
{"timestamp":"2026-08-20T11:00:22.588Z","request_id":"lab-000010","method":"GET","path":"/instance","status":200,"upstream":"172.23.0.12:8080","upstream_status":"200","request_time":0.088,"client":"192.0.2.24"}

# investigating each of these logs by request id in each log file

grep '"request_id":"lab-000122"' access.log
{"timestamp":"2026-08-20T11:05:02.503Z","request_id":"lab-000122","method":"GET","path":"/health","status":502,"upstream":"172.23.0.12:8080","upstream_status":"502","request_time":0.003,"client":"192.0.2.24"}

grep "lab-000122" error.log
2026/08/20 11:05:02 [error] 31#31: *122 connect() failed (111: Connection refused) while connecting to upstream, request_id=lab-000122, request: "GET /health HTTP/1.1", upstream: "http://172.23.0.12:8080/health"

grep '"request_id": "lab-000122"' application.log
(no output - request never reached the app)


grep '"request_id":"lab-000010"' access.log
{"timestamp":"2026-08-20T11:00:22.588Z","request_id":"lab-000010","method":"GET","path":"/instance","status":200,"upstream":"172.23.0.12:8080","upstream_status":"200","request_time":0.088,"client":"192.0.2.24"}

grep "lab-000010" error.log
(no output - no error logged for this request)

grep '"request_id": "lab-000010"' application.log
{"timestamp": "2026-08-20T11:00:22.588Z", "level": "INFO", "event": "http_request", "request_id": "lab-000010", "instance_id": "app-02", "method": "GET", "path": "/instance", "status": 200, "duration_ms": 88.0}
```
### Q9: Which errors appear to be proxy/connectivity issues versus dependency/application issues? What proves it?

```
# get every request_id error.log complained about (both refused + timeout)
grep -o 'request_id=lab-[0-9]*' error.log | sed 's/request_id=//' | sort -u > error_ids.txt
wc -l error_ids.txt
67

# split into connect-refused ids and timeout ids
grep "Connection refused" error.log | grep -o 'request_id=lab-[0-9]*' | sed 's/request_id=//' > refused_ids.txt
wc -l refused_ids.txt
59

grep "timed out" error.log | grep -o 'request_id=lab-[0-9]*' | sed 's/request_id=//' > timeout_ids.txt
wc -l timeout_ids.txt
8

# for each group, check if application.log has a matching entry
while read id; do grep -q "\"request_id\": \"$id\"" application.log && echo found; done < refused_ids.txt | wc -l
19
while read id; do grep -q "\"request_id\": \"$id\"" application.log && echo found; done < timeout_ids.txt | wc -l
8

# what does one of those timeout app.log entries actually say?
grep "\"request_id\": \"lab-000606\"" application.log
{"timestamp": "2026-08-20T11:25:15.200Z", "level": "INFO", "event": "http_request", "request_id": "lab-000606", "instance_id": "app-02", "method": "GET", "path": "/records", "status": 200, "duration_ms": 2700}

# now the other direction: does any dependency_error id show up in error.log?
grep '"event": "dependency_error"' application.log | grep -o '"request_id": "lab-[0-9]*"' | sed 's/.*"\(lab-[0-9]*\)"/\1/' > dep_ids.txt
wc -l dep_ids.txt
47
while read id; do grep -q "$id" error.log && echo found; done < dep_ids.txt | wc -l
0

# what final status do those dependency_error requests get in access.log?
while read id; do grep -o "\"request_id\":\"$id\",.*\"status\":[0-9]*" access.log; done < dep_ids.txt | grep -o '"status":[0-9]*' | sort | uniq -c
     47 "status":503

```
### Q10: What do the logs not prove? What would you check next in a running environment?
doesn't need commands

## Results
### Q1: What UTC interval is covered? How many valid, malformed and duplicate lines are in each file?

Interval covered: 2026-08-20, 11:00:00.015 - 11:29:57.578 UTC

access.log: there are 726 total lines (725 valid, 1 malformed, 5 duplicates)

error.log: there are 68 total lines (68 valid, 0 malformed, 0 duplicate lines)

application.log: there are 730 total lines (729 valid, 1 malformed, 2 duplicate lines)

### Q2: How many distinct client requests occurred? How did you deduplicate and avoid counting retries twice?
720 distinct requests + 5 duplicate lines + 1 malformed line

### Q3: What are the final client status counts and error rate? State your denominator.
Denominator: 720 (distinct client requests)
  200 -> 615
  404 -> 10
  502 -> 40
  503 -> 47
  504 -> 8

### Q4:
**Error 502** have 40 requests and paths are: /,/counter,/health,/records (10 for each path) also, time window was between 11:05:02-11:09:57 and the requested backend was only 172.23.0.12

**Error 503** have 47 requests and paths are: /ready(23 request),/counter(16),/records(8) also, time window was between 11:12:09-11:21:45 and requested backend was split between two backends (172.23.0.11:8080 and 172.23.0.12:8080)

**Error 504** have 8 requests and the only path was /records and time window was between 11:25:14-11:26:47 and requested backend was between split evenly between "172.23.0.11:8080" and "172.23.0.12:8080"

### Q5: What are the median and p95 client latencies? State the percentile method and units.
n = 720 (all distinct client requests, including successes and failures)
Median latency: 0.054 seconds = 54 ms
p95 latency: 2.001 seconds = 2001 ms

### Q6: Which requests retried upstream? How many succeeded after retrying?
19 requests retried to a second upstream backend. All 19 was succeeded after retrying (every one ended with status 200)

### Q7:
Everything explained in the timeline and correlated examples

### Q8: 8. Show one correlated failed request and one successful request. Include IDs and timestamps.
Failed request: lab-000122, GET /health, 2026-08-20T11:05:02.503Z, status 502
Successful request: lab-000010, GET /instance, 2026-08-20T11:00:22.588Z, status 200

### Q9:Which errors appear to be proxy/connectivity issues versus dependency/application issues? What proves it?
Proxy/connectivity issues (67 total, all from error.log):
  - 59 "Connection refused" - 40 of these never reach the app at all (no application.log entry); 19 retry to a second backend and succeed.
  - 8 "upstream timed out" - all 8 DO have an application.log entry, with status 200 and duration_ms=2700 The app finished the request, just slower than nginx's timeout window allowed.

Dependency/application issues (47 total, all from application.log):
  - 47 "dependency_error" events (31 redis TimeoutError, 16 postgres InvalidPassword). None of these appear in error.log at all.
  - All 47 map to a 503 in access.log.
### Q10: What do the logs not prove? What would you check next in a running environment?
doesn't need results

## Timeline and correlated examples
### Q4:
between 11:05:02 and 11:09:57  all errors 502 hit 172.23.0.12 only and this backend was unreachable
between 11:12:09 and 11:21:45  all resulted error 503 requests spread across both backends and wasn't a single-backend response
between 11:25:14 and 11:26:47  all resulted 504 (timeouts) also, requests spread evenly across both backend servers

so,

from what i have observed from 502 error logs it was pointing to a single-backend problem which is every one of the 40 failures went to 172.23.0.12 only during a 5 minute window from 11:05 to 11:09 with that one backend which indicate that it was down or unreachable and nginx couldn't even open a TCP connection to that backend. application.log has NO entries for these request_ids at all. the request never reached the app. This proves it's a pure infrastructure/connectivity failure: the app-02 process or container was down or unreachable, not an application bug.

503s (11:12-11:21): error.log is completely silent during this window (0 matching lines) - nginx never saw a connection or timeout problem, because it DID get a response from the backend. application.log instead shows 47 "dependency_error" events, all with dependency: redis, error_type: TimeoutError, spread across BOTH app-01 and app-02. This proves the 503s are an application layer issue: the app itself was timing out trying to reach Redis, then correctly returned a 503 to nginx. Since both instances are affected, it's Redis (or the network path to it)

504s (11:25-11:26): error.log shows 8 "upstream timed out" lines, alternating between 172.23.0.12 and 172.23.0.11 - nginx waited for a response header and got nothing back in time, from either backend. application.log has no entries for these request_ids either, meaning the app never finished processing (or never even got the request in time) consistent with both instances being briefly overloaded or unresponsive at the same moment, rather than one backend being down.

### Q6: Which requests retried upstream? How many succeeded after retrying?
All 19 retries happened between 11:05:07 and 11:09:52 - inside the same 502 outage window identified in Q4, where 172.23.0.12 was unreachable. what is interesting was their request_ids (lab-000124 through lab-000232) fall in the same range as the 40 requests that got a bare 502 with no retry which mean during that same outage, some requests retried and recovered, while others didn't retry at all and just failed.

### Q7: Build an incident timeline using evidence from access, error AND application logs.

11:00:00 - Log collection window starts. Traffic normal (200s across all paths).

11:05:02 - 11:09:57  BACKEND OUTAGE (172.23.0.12 unreachable)
  error.log:   58 "connect() failed (Connection refused)" lines, all -> 172.23.0.12
  access.log:  40 requests fail with 502 (no retry configured for their path)
               19 requests retry to 172.23.0.11 and succeed (200)
  app.log:     no entries for these request_ids - app-02 never received them

11:12:09 - 11:15:52  REDIS TIMEOUTS (both app instances affected)
  app.log:     31 "dependency_error" events, dependency=redis, error_type=TimeoutError,
               spread across app-01 and app-02
  access.log:  matching requests return 503, request_time ~2.0-2.025s
  error.log:   silent - nginx received a valid (if slow) HTTP response

11:20:07 - 11:21:45  POSTGRES AUTH FAILURES (both app instances affected)
  app.log:     16 "dependency_error" events, dependency=postgres, error_type=InvalidPassword,
               spread across app-01 and app-02
  access.log:  matching requests also return 503
  error.log:   silent, same reason as above

11:25:14 - 11:26:47  UPSTREAM TIMEOUTS (both backends)
  error.log:   8 "upstream timed out" lines, alternating 172.23.0.12 / 172.23.0.11
  access.log:  8 requests get 504, all on /records
  app.log:     no entries - app never finished responding in time

11:29:57 - Last access.log entry, status 200 - traffic back to normal.
11:30:00 - error.log "notice: log collector rotated stream" - end of window.

## Q8: 8. Show one correlated failed request and one successful request. Include IDs and timestamps.

lab-000122 (FAILED):
  11:05:02.503  access.log:  client gets 502 in 3ms, upstream=172.23.0.12
  11:05:02      error.log:   nginx logs "connect() failed, Connection refused" to 172.23.0.12
  --            app.log:     no entry - the request never reached app-02 at all
  This is a proxy-level failure: nginx couldn't even establish a TCP connection, so the request died before the application ever saw it.

lab-000010 (SUCCESSFUL):
  11:00:22.588  access.log:  client gets 200 in 88ms, upstream=172.23.0.12
  --            error.log:   no entry - no problem to log
  11:00:22.588  app.log:     app-02 logs the same request_id, same timestamp, same path, status 200 duration_ms=88.0 an exact match to what nginx recorded

so, This is the normal, healthy path: nginx forwards the request, the app instance handles it and logs it, and the timestamps/duration line up exactly between access.log and application.log.

## Q9: Which errors appear to be proxy/connectivity issues versus dependency/application issues? What proves it?
lab-000122 (connectivity, no retry):
  error.log: "connect() failed, Connection refused" -> 172.23.0.12
  application.log: nothing - the request never got past nginx

lab-000606 (connectivity, timeout):
  error.log: "upstream timed out" at 11:25:14
  application.log: app-02 returned status 200 at 11:25:15.200, duration_ms=2700
  The app actually succeeded - nginx just gave up waiting before the
  response came back.

lab-000292 (dependency/application):
  application.log: dependency_error, dependency=redis, error_type=TimeoutError
  error.log: nothing - nginx received a normal HTTP response (503), so
  there was no connection problem to log

## Q10: What do the logs not prove? What would you check next in a running environment?
doesn't need timeline

## Conclusions and limits

### Q1: What UTC interval is covered? How many valid, malformed and duplicate lines are in each file?
The malformed lines (line 311 in access.log, line 401 in application.log) are cut off mid-write also, they didn't have a closing brace or the rest of their fields

### Q2: How many distinct client requests occurred? How did you deduplicate and avoid counting retries twice?
Deduplication: I extracted the request_id field from every line and used sort -u, which collapses any repeated request_id down to one. This removes the 5 exact duplicate lines from Q1 (same request logged twice) without touching anything else.

Avoiding double-counting retries: a retry in this system is not logged as two separate lines. When nginx fails over to a second backend, it writes ONE access.log line for that request, with a comma inside the "upstream" field (e.g. "172.23.0.12:8080, 172.23.0.11:8080") showing both attempts. Since it's already a single line, sort -u leaves it alone - there was never a risk of counting it twice. I found 19 such retried requests this way.

### Q3: What are the final client status counts and error rate? State your denominator.
We had the dominator was 720 (total number of non-duplicate requests)

and we counted numbers of erros was:
    615 "status":200
     10 "status":404
     40 "status":502
     47 "status":503
      8 "status":504

Error Rate = (Number of Failed Requests / Total Number of Requests) × 100
which is (40+47+8/720) * 100 = 13.19 % (I didn't consider  the number of 404s because, this doesn't count as a service faliure it simply the page not found)
but, if we consider it as an error the error rate will be ((10+40+47+8/720) * 100 = 14.58 %)

### Q4:
Path pattern 502s hit /,/counter,/health,/records evenly so, 502 is backend-down, because, every path fails equally but, in  503 requests concentrates on endpoints that likely touch Redis in their handler like: /ready and /counter, while /health probably doesn't call Redis at all and stayed healthy throughout.

### Q5: What are the median and p95 client latencies? State the percentile method and units.
The gap between median (54 ms) and p95 (2001 ms) is explained by Q4's findings: the 47 requests that hit the Redis timeout (503s) each took almost exactly 2.0-2.025 seconds, and there are enough of them (47/720 = 6.5%) to sit right at the 95th percentile mark it is essentially measuring "how long a Redis-timeout request takes,"


### Q6: Which requests retried upstream? How many succeeded after retrying?
19 of 19 retried requests succeeded which indicates that the retry logic itself works fine when it triggers.

The bigger finding is which requests did retry: only /ready and /instance paths ever show a comma-separated upstream field. The other paths that hit the same dead backend during the same window (/, /health, /counter, /records and the 40 requests behind the 502s in Q4) never retried at all, they just failed outright. This points to nginx's proxy_next_upstream (retry-on-failure) setting only being enabled for /ready and /instance, not for the other locations - a configuration gap rather than a random failure. If the other paths had the same retry setting, most or all of those 40 failed requests likely would have succeeded too.

### Q7: Build an incident timeline using evidence from access, error AND application logs.

The 30-minute window contains four distinct, back-to-back incidents, not one continuous outage:
  1. Infrastructure: 172.23.0.12 unreachable (connection refused)
  2. Application: Redis timeouts on both instances
  3. Application: Postgres authentication failures on both instances
  4. Infrastructure: both backends briefly timed out under load

Limits: the logs don't explain WHY 172.23.0.12 refused connections, why Redis was timing out, or why Postgres suddenly started rejecting the app's password that would need infrastructure/orchestrator logs and the Postgres/Redis server-side logs.

### Q8: 8. Show one correlated failed request and one successful request. Include IDs and timestamps.
The presence or absence of an application.log entry is itself diagnostic: a request that completed normally always has a matching app.log line. a request that failed before ever reaching the app has none. That same signal is what separates proxy/connectivity failures from application-layer


### Q9: Which errors appear to be proxy/connectivity issues versus dependency/application issues? What proves it?

The proof is whether application.log has a matching entry:
  - error.log entry + no application.log entry -> the request never reached the app - a pure proxy/connectivity failure.
  - error.log entry + application.log entry showing a late success -> the app could handle the request, but not within nginx's timeout window - a timeout-tuning issue, not a hard outage.
  - application.log dependency_error + no error.log entry -> the app itself
    hit a broken dependency and correctly reported it as a 503; nginx never saw a connectivity problem.

Limits: this doesn't explain WHY 172.23.0.12 refused connections, why /records takes 2.7s under load, or why Postgres started rejecting the app's credentials - that needs infrastructure and database-side logs that aren't part of those log files.


### Q10: What do the logs not prove? What would you check next in a running environment?
What the logs prove: the timing, the request paths affected, the status codes, and which layer (proxy vs application) each failure happened at - because access.log, error.log, and application.log all agree with each other on timestamps and request_ids.

What the logs do NOT prove:

  - WHY 172.23.0.12 refused connections during 11:05-11:09 (crashed process? container restarted? out of memory? deployment in progress?)
  - the logs only show the symptom (refused connections), not the cause.

  - WHY Redis was timing out during 11:12-11:15 - could be Redis itself overloaded, a network problem between the app and Redis, or Redis being restarted. None of that is visible from application.log alone.

  - WHY Postgres started rejecting the app's password during 11:20-11:21 - could be a credential rotation config push, or a typo in a secret. The logs only show the app was rejected, not what changed on the Postgres side.

  - WHY /records specifically takes ~2.7 seconds under load (the cause behind the 11:25-11:26 timeouts) - no evidence of what /records does internally (a slow query? a slow downstream call?).

  - Whether this was a one-time incident or something that keeps recurring - this is only a 30-minute window, and the README says it's a subset of a longer incident, so I can't say if this pattern repeats.

  - User/business impact - the logs show status codes, not what those failures meant for actual users (lost transactions, retried by a client app, etc).

What I'd check next in a running environment:

  - Container/orchestrator events (docker events, kubectl describe pod, or equivalent) for 172.23.0.12 / app-02 around 11:05 and 11:09, to see if it crashed, was OOM-killed, or was redeployed.
  - Redis server-side logs and metrics (CPU, memory, connection count, slow log) for 11:12-11:15, to see if Redis itself was struggling.
  - Postgres server-side auth logs for 11:20-11:21, to check for a credential/secret rotation event around that time.
  - Application-level tracing or profiling on the /records endpoint to see what makes it take 2.7 seconds under load.
  - Whether nginx's proxy_next_upstream (retry) setting is intentionally limited to /ready and /instance, or if extending it to the other paths would reduce future 502s.
  - A longer time window of logs (before 11:00 and after 11:30) to see if this is a recurring pattern or a one-off incident.
