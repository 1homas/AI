#!/bin/bash

# Start Podman if not already running
podman machine start
# if [ $? -ne 0 ]; then echo "Already started!"; exit 1; fi
podman-compose -f ai_compose.yaml stop

# Pull the latest of each image for use
echo "Updating n8n..."
podman pull docker.n8n.io/n8nio/n8n
podman container rm n8n

echo "Updating ollama..."
podman pull ollama/ollama:latest

echo "Updating open-webui..."
podman pull ghcr.io/open-webui/open-webui:latest

echo "Updating portainer..."
podman pull portainer/portainer-ce:latest

echo "Updating alpine..."
podman pull alpine:latest

echo "Updating ubuntu..."
podman pull ubuntu:latest

podman-compose -f ai_compose.yaml up -d
