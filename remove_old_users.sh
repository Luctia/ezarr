#!/bin/bash

# shut down all ezarr containers referenced by docker-compose.yml 
# If you previously had ezarr installed somewhere else you have to do this manually in the directory where the docker-compose file is.
sudo docker compose down

# Remove old users and group
sudo userdel sonarr
sudo userdel radarr
sudo userdel lidarr
sudo userdel readarr
sudo userdel mylar
sudo userdel audiobookshelf
sudo userdel bazarr
sudo userdel prowlarr
sudo userdel jackett
sudo userdel plex
sudo userdel overseerr
sudo userdel jellyseerr
sudo userdel qbittorrent
sudo userdel sabnzbd
sudo groupdel mediacenter

