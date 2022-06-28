#!/bin/bash

# Make users and group
sudo useradd sonarr
sudo useradd radarr
sudo useradd lidarr
sudo useradd prowlarr
sudo useradd qbittorrent
sudo groupadd mediacenter
sudo usermod -a -G mediacenter sonarr
sudo usermod -a -G mediacenter radarr
sudo usermod -a -G mediacenter lidarr
sudo usermod -a -G mediacenter prowlarr
sudo usermod -a -G mediacenter qbittorrent

# Make directories
sudo mkdir docker data
sudo mkdir docker/sonarr-config docker/radarr-config docker/lidarr-config docker/prowlarr-config docker/qbittorrent-config
sudo mkdir data/torrents data/media
sudo mkdir data/torrents/tv data/torrents/movies data/torrents/music data/media/tv data/media/movies data/media/music

# Set permissions
sudo chmod -R 775 data/
sudo chown -R 1000:mediacenter data/
sudo chown -R sonarr:mediacenter docker/sonarr-config
sudo chown -R radarr:mediacenter docker/radarr-config
sudo chown -R lidarr:mediacenter docker/lidarr-config
sudo chown -R prowlarr:mediacenter docker/prowlarr-config
sudo chown -R qbittorrent:mediacenter docker/qbittorrent-config

sonarr_id=$(sudo cat /etc/passwd | grep sonarr | cut -c 10-13)
radarr_id=$(sudo cat /etc/passwd | grep radarr | cut -c 10-13)
lidarr_id=$(sudo cat /etc/passwd | grep lidarr | cut -c 10-13)
prowlarr_id=$(sudo cat /etc/passwd | grep prowlarr | cut -c 12-15)
qbit_id=$(sudo cat /etc/passwd | grep qbittorrent | cut -c 15-18)

echo "SONARR_UID=${sonarr_id}" >> .env
echo "RADARR_UID=${radarr_id}" >> .env
echo "LIDARR_UID=${lidarr_id}" >> .env
echo "PROWLARR_UID=${prowlarr_id}" >> .env
echo "QBIT_UID=${qbit_id}" >> .env
