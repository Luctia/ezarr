#!/bin/bash

# Shutds down all the containers, updates them and removes the old images. 
# If you want to keep the old images remove or comment the last line.

# If the following commands throw permission errors, uncomment the following lines
#sudo groupadd docker
#sudo usermod -aG docker $USER
#newgrp docker
# if that isnt enough then reboot

docker compose pull
docker compose up -d
docker image prune -f
