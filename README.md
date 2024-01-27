# EZARR
[![Check running](https://github.com/Luctia/ezarr/actions/workflows/check_running.yml/badge.svg)](https://github.com/Luctia/ezarr/actions/workflows/check_running.yml)

Ezarr is a project built to make it EZ to deploy a Servarr mediacenter on an Ubuntu server. The
badge above means that the shell script and docker-compose file in this repository at least *don't
crash*. It doesn't necessarily mean it will run well on your system ;) It features:
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

## Using
### Using the CLI
To make things easier, a CLI has been developed. First, clone the repository in a directory of your
choosing. You can run it by entering `python main.py` and the CLI will guide you through the
process. Please take a look at [important notes](#important-notes) before you continue.

### Manually
1. To get started, clone the repository in a directory of your choosing. **Note: this will be where
   your installation and media will be as well, so think about this a bit.**
2. Copy `.env.sample` to a real `.env` by running `$ cp .env.sample .env`.
3. Set the environment variables to your liking. Note that `ROOT_DIR` should be the directory you
   have cloned this in.
4. Run `setup.sh` as superuser. This will set up your users, a system of directories, ensure
   permissions are set correctly and sets some more environment variables for docker compose.
5. Take a look at the `docker-compose.yml` file. If there are services you would like to ignore
   (for example, running PleX and Jellyfin at the same time is a bit unusual), you can comment them
   out by placing `#` in front of the lines. This ensures they are ignored by Docker compose.
6. Run `docker compose up`.

That's it! Your containers are now up and you can continue to set up the settings in them. Please
take a look at [important notes](#important-notes) before you continue.

## Important notes
- When linking one service to another, remember to use the container name instead of `localhost`.
- Please set the settings of the -arr containers as soon as possible to the following (use
  advanced):
  - Media management:
    - Use hardlinks instead of Copy: `true`
    - Root folder: `/data/media/` and then tv, movies or music depending on service
  - Make sure to set a username and password for all servarr services and qBittorrent!
- In qBittorrent, after connecting it to the -arr services, you can indicate it should move
  torrents in certain categories to certain directories, like torrents in the `radarr` category
  to `/data/torrents/movies`. You should do this. Also set the `Default Save Path` to
  `/data/torrents`. Set "Run external program on torrent completion" to true and enter this in the
  field: `chmod -R 775 "%F/"`.
- You'll have to add indexers in Prowlarr by hand. Use Prowlarrs settings to connect it to the
  other -arr apps.
  
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
If you'd like to update containers, you can move to the directory of your `docker-compose.yml` file
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
