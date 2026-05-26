#!/usr/bin/env bash

set -e

echo "====================================="
echo "Starting Samruddhi Deployment"
echo "====================================="

export PYTHONUNBUFFERED=1

echo "[1/5] Loading environment variables..."

if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
fi

echo "[2/5] Starting Docker services..."

docker-compose up -d --build

echo "[3/5] Waiting for services..."

sleep 10

echo "[4/5] Running health checks..."

curl http://localhost:8000/tools/health

echo "[5/5] Deployment complete."

echo "====================================="
echo "Samruddhi deployment active"
echo "====================================="