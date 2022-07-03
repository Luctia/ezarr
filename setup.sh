#!/bin/bash

# Make users and group
sudo useradd sonarr
sudo useradd radarr
sudo useradd lidarr
sudo useradd readarr
sudo useradd mylar
sudo useradd prowlarr
sudo useradd qbittorrent
sudo groupadd mediacenter
sudo usermod -a -G mediacenter sonarr
sudo usermod -a -G mediacenter radarr
sudo usermod -a -G mediacenter lidarr
sudo usermod -a -G mediacenter readarr
sudo usermod -a -G mediacenter mylar
sudo usermod -a -G mediacenter prowlarr
sudo usermod -a -G mediacenter qbittorrent

# Make directories
sudo mkdir docker data
sudo mkdir docker/sonarr-config docker/radarr-config docker/lidarr-config docker/readarr-config docker/mylar-config docker/prowlarr-config docker/qbittorrent-config
sudo mkdir data/torrents data/media
sudo mkdir data/torrents/tv data/torrents/movies data/torrents/music data/torrents/books data/torrents/comics data/media/tv data/media/movies data/media/music data/media/books data/media/comics

# Set permissions
sudo chmod -R 775 data/
sudo chown -R 1000:mediacenter data/
sudo chown -R sonarr:mediacenter docker/sonarr-config
sudo chown -R radarr:mediacenter docker/radarr-config
sudo chown -R lidarr:mediacenter docker/lidarr-config
sudo chown -R readarr:mediacenter docker/readarr-config
sudo chown -R mylar:mediacenter docker/mylar-config
sudo chown -R prowlarr:mediacenter docker/prowlarr-config
sudo chown -R qbittorrent:mediacenter docker/qbittorrent-config

sonarr_id=$(sudo cat /etc/passwd | grep sonarr | cut -c 10-13)
radarr_id=$(sudo cat /etc/passwd | grep radarr | cut -c 10-13)
lidarr_id=$(sudo cat /etc/passwd | grep lidarr | cut -c 10-13)
readarr_id=$(sudo cat /etc/passwd | grep readarr | cut -c 11-14)
mylar_id=$(sudo cat /etc/passwd | grep mylar | cut -c 9-12)
prowlarr_id=$(sudo cat /etc/passwd | grep prowlarr | cut -c 12-15)
qbit_id=$(sudo cat /etc/passwd | grep qbittorrent | cut -c 15-18)
group_id=$(sudo cat /etc/group | grep mediacenter | cut -c 15-18)

echo "SONARR_UID=${sonarr_id}" >> .env
echo "RADARR_UID=${radarr_id}" >> .env
echo "LIDARR_UID=${lidarr_id}" >> .env
echo "READARR_UID=${readarr_id}" >> .env
echo "MYLAR_UID=${mylar_id}" >> .env
echo "PROWLARR_UID=${prowlarr_id}" >> .env
echo "QBIT_UID=${qbit_id}" >> .env
echo "MEDIACENTER_GID=${group_id}" >> .env
