
import requests
import subprocess
import time

BASE_URL = "http://127.0.0.1:8080"


def get_instance():
    try:
        r = requests.get(BASE_URL + "/instance", timeout=5)
        return r.status_code, r.json().get("instance_id")
    except requests.RequestException:
        return None, None


print("=== Failure Test: app-01 ===")

# 1. Stop app-01
print("\nStopping app-01...")

subprocess.run(
    ["docker", "stop", "app-01"],
    check=True
)

time.sleep(2)


# 2. Send requests while app-01 is down
print("\nTesting while app-01 is stopped...")

success = 0
errors = 0
instances = set()

for _ in range(10):
    status, instance = get_instance()

    if status == 200:
        success += 1
        instances.add(instance)
        print(f"[PASS] 200 from {instance}")
    else:
        errors += 1
        print("[ERROR] Request failed")

print(f"\nSuccessful requests: {success}")
print(f"Failed requests: {errors}")
print(f"Instances reached: {instances}")


# 3. Verify app-02 is still serving
if "app-02" in instances:
    print("[PASS] app-02 continued serving requests")
else:
    print("[FAIL] app-02 did not serve requests")


# 4. Restore app-01
print("\nStarting app-01 again...")

subprocess.run(
    ["docker", "start", "app-01"],
    check=True
)

time.sleep(5)


# 5. Prove recovery
print("\nTesting after recovery...")

status, instance = get_instance()

if status == 200:
    print(f"[PASS] Request succeeded after recovery: {instance}")
else:
    print("[FAIL] Request failed after recovery")