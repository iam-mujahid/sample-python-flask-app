#!/bin/bash
set -e

# Stop the running container (if any)
echo "Hi"
#  cleaning the previous containers

# docker ps

docker stop  flask-app-container || true
docker rm -f flask-app-container || true


