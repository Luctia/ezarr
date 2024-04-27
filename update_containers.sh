#!/bin/bash

# Shutds down all the containers, updates them and removes the old images. 
# If you want to keep the old images remove or comment the last line.

sudo docker-compose pull
sudo docker-compose down
sudo docker-compose up -d
sudo docker image prune -f
