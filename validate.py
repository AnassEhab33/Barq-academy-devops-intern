
import requests
import subprocess
import sys

BASE_URL = "http://127.0.0.1:8080"

passed = 0
failed = 0


def check(condition, message):
    global passed, failed

    if condition:
        print("[PASS]", message)
        passed += 1
    else:
        print("[FAIL]", message)
        failed += 1


def get(path):
    try:
        return requests.get(
            BASE_URL + path,
            timeout=5,
            headers={"Connection": "close"}
        )
    except requests.RequestException as e:
        print("[ERROR]", path, e)
        return None


def docker_inspect(container):
    try:
        result = subprocess.run(
            ["docker", "inspect", container],
            capture_output=True,
            text=True,
            check=True
        )

        import json
        return json.loads(result.stdout)[0]

    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


# ------------------------------------------------------------
# Endpoint Validation
# ------------------------------------------------------------

print("=== Endpoint Validation ===")

# /
r = get("/")
check(
    r is not None and r.status_code == 200,
    "GET / returns 200"
)

if r:
    try:
        data = r.json()

        check(
            data.get("message") == "Welcome to BARQ Systems",
            "GET / contains the expected message"
        )

        check(
            bool(data.get("instance_id")),
            "GET / contains instance_id"
        )
    except ValueError:
        check(False, "GET / returns valid JSON")


# /health
r = get("/health")

check(
    r is not None and r.status_code == 200,
    "GET /health returns 200"
)


# /ready
r = get("/ready")

check(
    r is not None and r.status_code == 200,
    "GET /ready returns 200"
)

if r:
    try:
        data = r.json()
        dependencies = data.get("dependencies", {})

        check(
            dependencies.get("postgres") == "ready",
            "PostgreSQL is ready"
        )

        check(
            dependencies.get("redis") == "ready",
            "Redis is ready"
        )

    except ValueError:
        check(False, "/ready returns valid JSON")


# /instance
r = get("/instance")

check(
    r is not None and r.status_code == 200,
    "GET /instance returns 200"
)

if r:
    try:
        data = r.json()

        check(
            bool(data.get("instance_id")),
            "/instance contains instance_id"
        )

        check(
            data.get("instance_id") == r.headers.get("X-Instance-ID"),
            "instance_id matches X-Instance-ID"
        )

    except ValueError:
        check(False, "/instance returns valid JSON")


# ------------------------------------------------------------
# PostgreSQL Validation
# ------------------------------------------------------------

print("\n=== PostgreSQL Validation ===")

title = "Validation persistence proof"

try:
    r = requests.post(
        BASE_URL + "/records",
        json={"title": title},
        timeout=5
    )

    check(
        r.status_code == 201,
        "POST /records returns 201"
    )

    r = get("/records")

    check(
        r is not None and r.status_code == 200,
        "GET /records returns 200"
    )

    if r:
        records = r.json().get("records", [])

        check(
            any(record.get("title") == title for record in records),
            "Created record persists in PostgreSQL"
        )

except requests.RequestException as e:
    print("[ERROR] PostgreSQL test:", e)
    check(False, "PostgreSQL requests completed")


# ------------------------------------------------------------
# Redis Validation
# ------------------------------------------------------------

print("\n=== Redis Validation ===")

r1 = get("/counter")
r2 = get("/counter")

check(
    r1 is not None and r1.status_code == 200,
    "First /counter request returns 200"
)

check(
    r2 is not None and r2.status_code == 200,
    "Second /counter request returns 200"
)

if r1 and r2:
    try:
        first = r1.json()["counter"]
        second = r2.json()["counter"]

        check(
            second == first + 1,
            "Redis counter increments by one"
        )

    except (KeyError, ValueError):
        check(False, "Counter returns a valid value")


# ------------------------------------------------------------
# Input Validation
# ------------------------------------------------------------

print("\n=== Input Validation ===")

r = requests.post(
    BASE_URL + "/records",
    json={"title": ""},
    timeout=5
)

check(
    r.status_code == 400,
    "Empty title returns 400"
)


r = requests.post(
    BASE_URL + "/records",
    json={"title": "A" * 201},
    timeout=5
)

check(
    r.status_code == 400,
    "Title longer than 200 characters returns 400"
)


# ------------------------------------------------------------
# 404 Validation
# ------------------------------------------------------------

print("\n=== 404 Validation ===")

r = get("/does-not-exist")

check(
    r is not None and r.status_code == 404,
    "Unknown route returns 404"
)


# ------------------------------------------------------------
# Both Backends
# ------------------------------------------------------------

print("\n=== Backend Load Balancing ===")

instances = set()

for _ in range(20):
    r = get("/instance")

    if r and r.status_code == 200:
        try:
            instances.add(r.json()["instance_id"])
        except (KeyError, ValueError):
            pass

print("Instances seen:", instances)

check(
    "app-01" in instances,
    "Requests reached app-01"
)

check(
    "app-02" in instances,
    "Requests reached app-02"
)


# ------------------------------------------------------------
# Port Exposure
# ------------------------------------------------------------

print("\n=== Port Exposure ===")

expected = {
    "nginx": True,
    "app-01": False,
    "app-02": False,
    "postgres": False,
    "redis": False,
}

for container, should_have_ports in expected.items():

    info = docker_inspect(container)

    if info is None:
        check(False, f"Can inspect {container}")
        continue

    ports = info["NetworkSettings"]["Ports"]

    published = {
        container_port: bindings
        for container_port, bindings in ports.items()
        if bindings
    }

    print(f"{container} published ports: {published}")

    if should_have_ports:
        check(
            bool(published),
            f"{container} has its intended public port published"
        )
    else:
        check(
            not published,
            f"{container} has no host-published ports"
        )


# ------------------------------------------------------------
# Network Isolation
# ------------------------------------------------------------

print("\n=== Network Isolation ===")

expected_networks = {
    "frontend": {
        "nginx",
        "app-01",
        "app-02",
    },
    "backend": {
        "app-01",
        "app-02",
        "postgres",
        "redis",
    },
}

for network, expected_services in expected_networks.items():

    result = subprocess.run(
        [
            "docker",
            "network",
            "inspect",
            f"barq-assessment_{network}",
            "-f",
            "{{range .Containers}}{{.Name}} {{end}}",
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        check(
            False,
            f"{network} network exists"
        )
        continue

    actual_services = set(result.stdout.split())

    print(f"{network} connected services: {actual_services}")

    check(
        actual_services == expected_services,
        f"{network} has the expected services"
    )


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("\n==============================")
print("Validation Summary")
print("==============================")

print(f"Passed: {passed}")
print(f"Failed: {failed}")

if failed:
    print("\nVALIDATION FAILED")
    sys.exit(1)
else:
    print("\nVALIDATION PASSED")
    sys.exit(0)

