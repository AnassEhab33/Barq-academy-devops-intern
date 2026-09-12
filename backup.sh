#!/bin/bash

BACKUP_FILE="records_backup.sql"

echo "=== PostgreSQL Backup ==="

echo "Creating backup..."

docker exec postgres pg_dump \
    -U barq_app \
    -d barq_tasks \
    --table=public.records \
    --clean \
    --if-exists \
    --no-owner \
    > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "[PASS] Backup created: $BACKUP_FILE"
else
    echo "[FAIL] Backup failed"
    exit 1
fi
