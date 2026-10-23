#!/bin/bash
set -e

echo "Cleaning up previous containers..."

# 1. Target the exact host binding string '0.0.0.0:5000'
container_id=$(docker ps | grep "0.0.0.0:5000" | awk '{print $1}')

# 2. Check if we found a dynamic ID
if [ -n "$container_id" ]; then
    echo "Found running container ID: $container_id blocking port 5000. Stopping it..."
    docker stop "$container_id"
    docker rm -f "$container_id"
else
    # 3. Fallback: Try to clean up by the explicit static name just in case
    echo "No container found via port filtering. Attempting static name removal..."
    docker stop flask-app-container || true
    docker rm -f flask-app-container || true
fi

echo "Port 5000 is now completely cleared!"
