#!/bin/bash

BACKUP_FILE="records_backup.sql"

echo "=== PostgreSQL Restore ==="

if [ ! -f "$BACKUP_FILE" ]; then
    echo "[FAIL] Backup file not found"
    exit 1
fi

echo "Deleting current records..."

docker exec postgres psql \
    -U barq_app \
    -d barq_tasks \
    -c "DROP TABLE public.records;"

if [ $? -ne 0 ]; then
    echo "[FAIL] Could not delete records table"
    exit 1
fi

echo "[PASS] Current data removed"

echo "Restoring backup..."

docker exec -i postgres psql \
    -U barq_app \
    -d barq_tasks \
    < "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "[PASS] Backup restored"
else
    echo "[FAIL] Restore failed"
    exit 1
fi

echo "Verifying restored data..."

docker exec postgres psql \
    -U barq_app \
    -d barq_tasks \
    -c "SELECT * FROM records;"

if [ $? -eq 0 ]; then
    echo "[PASS] Restored data verified"
else
    echo "[FAIL] Could not verify restored data"
    exit 1
fi
