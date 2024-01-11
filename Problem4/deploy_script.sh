#!/bin/bash

# Set the variables
DOCKER_USERNAME="devongo"
DOCKER_TOKEN="dckr_pat_NtSTq0zI-HAEGw1qfmHw-W_C3o8"
DOCKER_IMAGE_NAME="saic-image"
DOCKER_IMAGE_TAG="latest"
NEW_DOCKER_IMAGE_TAG="v1.0" # Specify the new tag here

# Log in to Docker Hub using the token
echo $DOCKER_TOKEN | docker login --username $DOCKER_USERNAME --password-stdin

# Tag the Docker image
docker tag $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG $DOCKER_USERNAME/$DOCKER_IMAGE_NAME:$NEW_DOCKER_IMAGE_TAG

# Push the Docker image to Docker Hub with the new tag
docker push $DOCKER_USERNAME/$DOCKER_IMAGE_NAME:$NEW_DOCKER_IMAGE_TAG
