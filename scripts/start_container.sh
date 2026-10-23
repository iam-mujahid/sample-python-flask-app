#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
echo "pulling the image from docker hub"
docker pull mujahidhub/simple-python-flask-app:latest


# Run the Docker image as a container
docker run -d -p --name flask-app-container 80:5000 mujahidhub/simple-python-flask-app:latest 
