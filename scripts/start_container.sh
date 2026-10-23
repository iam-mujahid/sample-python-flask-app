#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
echo "pulling the image from docker hub"
docker pull mujahidhub/simple-python-flask-app:latest


# Run the Docker image as a container
docker run -d -p 80:5000 --name flask-app-container 5000:5000 mujahidhub/simple-python-flask-app:latest 
