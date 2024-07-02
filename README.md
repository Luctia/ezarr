# EZARR
[![Check running](https://github.com/Luctia/ezarr/actions/workflows/check_running.yml/badge.svg)](https://github.com/Luctia/ezarr/actions/workflows/check_running.yml)

Ezarr is a project built to make it EZ to deploy a Servarr mediacenter on an Ubuntu server. The
badge above means that the shell script and docker-compose file in this repository at least *don't
crash*. It doesn't necessarily mean it will run well on your system ;) 
It's set up to follow the [TRaSH guidelines](https://trash-guides.info/Hardlinks/How-to-setup-for/Docker/) so it should at least perform optimally. It features:
- [Sonarr](https://sonarr.tv/) is an application to manage TV shows. It is capable of keeping track
  of what you'd like to watch, at what quality, in which language and more, and can find a place to
  download this if connected to Prowlarr and qBittorrent. It can also reorganize the media you
  already own in order to create a more uniformly formatted collection.
- [Radarr](https://radarr.video/) is like Sonarr, but for movies.
- [Bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr that manages
  and downloads subtitles based on your requirements.
- [Lidarr](https://lidarr.audio/) is like Sonarr, but for music.
- [Readarr](https://readarr.com/) is like Sonarr, but for books.
- [Mylar3](https://github.com/mylar3/mylar3) is like Sonarr, but for comic books. This one is a bit
  tricky to set up, so do so at your own risk. In order to connect this to your Prowlarr container,
  the process within Prowlarr is the same as for the other containers (add app). You'll have to add
  an API key within Mylar3, yourself.
- [Audiobookshelf](https://www.audiobookshelf.org/) is a self-hosted audiobook and podcast server.
- [Prowlarr](https://wiki.servarr.com/prowlarr) can keep track of indexers, which are services that
  keep track of Torrent or UseNet links. One can search an indexer for certain content and find a
  where to download this. **Note**: when adding an indexer, please do not set the "seed ratio" to
  less than 1. Less than 1 means that you upload less than you download. Not only is this
  unfriendly towards your fellow users, but it can also get you banned from certain indexers.
- [Jackett](https://github.com/Jackett/Jackett) is an alternative to Prowlarr. 
- [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) is a proxy server to bypass Cloudflare and DDoS-GUARD protection.
- [qBittorrent](https://www.qbittorrent.org/) can download torrents and provides a bunch more
  features for management.
- [SABnzbd](https://sabnzbd.org/) can download nzb's
  features for management.
- [PleX](https://www.plex.tv/) is a mediaserver. Using this, you get access to a Netflix-like
  interface across many devices like your laptop or computer, your phone, your TV and more. For
  some features, you need a [PleX pass](https://www.plex.tv/nl/plex-pass/).
- [Tautulli](https://tautulli.com/) is a monitoring application for PleX  which can keep track of
  what has been watched, who watched it, when and where they watched it, and how it was watched.
- [Jellyfin](https://jellyfin.org/) is an alternative for PleX. Which you'd like to use is a matter
  of preference, and you *could* even use both, although this is probably a waste of resources.
- [Overseerr](https://overseerr.dev/) is a show and movie request management and media discovery
   tool.
- [Jellyseerr](https://github.com/Fallenbagel/jellyseerr) is like Overseerr, but for Jellyfin.

## Requirements
Currently this script only works on Linux. There is a chance that the sample docker compose file will work on Windows, although untested.
The only requirements other than that are **Python 3** and **docker** with **docker-compose-v2**.
While this script _may_ work on docker-compose-v1 it's made to be and highly recommended to be run using v2.
The easiest way to install these dependencies on Ubuntu and other Debian-based distors is by running:
```
sudo apt-get install python3 docker.io docker-compose-v2
```
For other Linux distros you may have to use a different package manager or download directly from docker's website.

## Using
### Using the CLI
To make things easier, a CLI has been developed. First, clone the repository in a directory of your
choosing. You can run it by entering `python3 main.py` and the CLI will guide you through the
process. This is the recommended method if you're setting this up for the first time on a new system. 
Please take a look at [important notes](#important-notes) before you continue. 
**NOTE: This script will create users for each container with IDs ranging from 13001 to 13014. 
If you want to choose your own IDs (or some of them are occupied) you have to go through the manual install.**

### Manually
If you're installing this for the first time simply follow these steps. 
If you're coming from an older version or reinstalling with different IDs, run `remove_old_users.sh` to clean up old users and then follow these steps.
1. To get started, clone the repository in a directory of your choosing. `git clone https://github.com/Luctia/ezarr.git`
2. Copy `.env.sample` to a real `.env` by running `$ cp .env.sample .env`.
3. Set the environment variables to your liking. Pay special attention `ROOT_DIR` as this is where everything is going to be stored in. 
   The path in this value needs to be **absolute**. If you leave it empty it's going to install in the directory the .env file is currently in.
   `UID` should be set to the ID of the user that you want to run docker with. You can find this by running `id -u` from that user's shell.
4. Run `setup.sh` as superuser. This will set up your users, a system of directories and ensure permissions are set correctly.
5. Copy `docker-compose.yml.sample` to a real `docker-compose.yml` by running `$ cp docker-compose.yml.sample docker-compose.yml`.
6. Take a look at the `docker-compose.yml` file. If there are services you would like to ignore
   (for example, running PleX and Jellyfin at the same time is a bit unusual), you can comment them
   out by placing `#` in front of the lines. This ensures they are ignored by Docker compose. 
   Double check that your .env file is set up properly.
7. Run `docker compose up -d` to start the containers. If it complains about permissions run the following commands to add your current user to the docker group and apply changes:
    ```
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    ```
    If it still doesn't work reboot your system.

That's it! Your containers are now up and you can continue to set up the settings in them. Please
take a look at [important notes](#important-notes) before you continue.

## Important notes
- You probably shouldn't run the python script as root. Ideally you should create a brand new user that's just for these services, but any regular user will do.
  It will need your password for `sudo` to set up the permissions and folder structures, but you shouldn't run it *as* root.
- If you already used this script previously and want to clean up old users, run `remove_old_users.sh`.
  This is also recommended if you are updating from an earlier version of this script, since there were previously some conflicts in user IDs.
- It is recommended to restart your system after script completion, so that newly created users and groups can be loaded properly.
- When linking one service to another, remember to use the container name instead of `localhost`.
- Please set the settings of the -arr containers as soon as possible to the following (use
  advanced):
  - Media management:
    - Use hardlinks instead of Copy: `true`
    - Root folder: `/data/media/` and then tv, movies or music depending on service
  - qBittorrent ships with a default username `admin` and a one-time password that can be viewed by running `docker logs qbittorrent`.
  - Make sure to set a username and password for all servarr services and qBittorrent!
- In qBittorrent, after connecting it to the -arr services, you can indicate it should move
  torrents in certain categories to certain directories, like torrents in the `radarr` category
  to `/data/torrents/movies`. You should do this. Also set the `Default Save Path` to
  `/data/torrents`. Set "Run external program on torrent completion" to true and enter this in the
  field: `chmod -R 775 "%F/"`.
- You'll have to add indexers in Prowlarr by hand. Use Prowlarrs settings to connect it to the
  other -arr apps.

### IMPORTANT IF USING NFS SHARES
- NFS shares' permissions are mapped by user IDs. If you want to access a file as a client, your user ID needs to match the user ID of the owner (or group) of that file on the NFS server. 
Note that if you are a group member (and not the owner), having matching group IDs won't be enough, there also needs to be a corresponding user on the NFS server. The easiest way to make sure
the users and groups are set up on both sides correctly is to run `setup.sh` on both your NFS server and your client. 
On your server:
- Copy `.env` and `setup.sh` to your NFS server.
- You may have to adjust `.env` so that `ROOT_DIR` reflects where it will be stored on your server, which is most likely different from the mapped location on the client.
- Make sure that the `.env` file is not a .sample. Run `setup.sh`.
- Now follow all the same steps but on your client machine. Always double-check that `.env` is set correctly, especially `ROOT_DIR`.
You don't have to do this on your server first but it's recommended. If you are running this script on the client **make sure that you temporarily enable -no-root-squash on your NFS server**, 
as the script needs superuser privileges to run and by default on NFS the root user is mapped to nowhere to prevent abuse.
  
### SABnzbd External internet access denied message
When you're trying to access SABnzbd the first time you'll come across the message `External
internet access denied`. To fix this simple modify the `sabnzbd.ini` and change `inet_exposure` to
`4`, restart the docker container for sabnzbd (`docker restart sabnzbd`) and now you can access the
UI of SABnzbd (note: you may get a `Access denied - Hostname verification failed`, to fix this,
simply go to the IP of your server directly instead of the hostname). After accessing the UI don't
forget to set a username and password (https://sabnzbd.org/wiki/configuration/3.7/general,
section Security).

For more instructions or help see also https://sabnzbd.org/wiki/extra/access-denied.html on the
official SABnzbd website.

## FAQ

### How to update containers
There is an `update_containers.sh` script that takes care of this. Simply run it and it updates
all containers and removes old images. If you want to keep them, simply comment out the last line of the script.
It's essentially the following steps but automated:
If you'd like to it manually, go to the directory of your `docker-compose.yml` file
and run `(sudo) docker compose pull`. This pulls the newest versions of all images (blueprints for
containers) listed in the `docker-compose.yml` file. Then, you can run `(sudo) docker compose up
-d`. This will deploy the new versions without losing uptime. Afterwards, you can run `(sudo)
docker image prune` to remove the old images, freeing up space.

### Why do I need to set some settings myself, can that be added?
Some settings, particularly for the Servarr suite, are set in databases. While it *might* be
possible to interact with this database after creation, I'd rather not touch these. It's not
that difficult to set them yourself, and quite difficult to do it automatically. For other
containers, configuration files are automatically generated, so these are more easily edited,
but I currently don't believe this is worth the effort.

On top of the above, connecting the containers above would mean setting a password and creating an
API key for all of them. This would lead to everyone using Ezarr having the same API key and user/
password combination. Personally, I'd rather trust users to figure this out on their own rather
than trusting them to change these passwords and keys.
