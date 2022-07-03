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
- [Lidarr](https://lidarr.audio/) is like Sonarr, but for music.
- [Readarr](https://readarr.com/) is like Sonarr, but for books.
- [Mylar3](https://github.com/mylar3/mylar3) is like Sonarr, but for comic books. This one is a bit
  tricky to set up, so do so at your own risk. In order to connect this to your Prowlarr container,
  the process within Prowlarr is the same as for the other containers (add app). You'll have to add
  an API key within Mylar3, yourself.
- [Prowlarr](https://wiki.servarr.com/prowlarr) can keep track of indexers, which are services that
  keep track of Torrent or UseNet links. One can search an indexer for certain content and find a
  where to download this. **Note**: when adding an indexer, please do not set the "seed ratio" to
  less than 1. Less than 1 means that you upload less than you download. Not only is this
  unfriendly towards your fellow users, but it can also get you banned from certain indexers.
- [qBittorrent](https://www.qbittorrent.org/) can download torrents and provides a bunch more
  features for management.
- [PleX](https://www.plex.tv/) is a mediaserver. Using this, you get access to a Netflix-like
  interface across many devices like your laptop or computer, your phone, your TV and more. For
  some features, you need a [PleX pass](https://www.plex.tv/nl/plex-pass/).
- [Tautulli](https://tautulli.com/) is a monitoring application for PleX  which can keep track of
  what has been watched, who watched it, when and where they watched it, and how it was watched.
- [Jellyfin](https://jellyfin.org/) is an alternative for PleX. Which you'd like to use is a matter
  of preference, and you *could* even use both, although this is probably a waste of resources.

## Using
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

That's it! Your containers are now up and you can continue to set up the settings in them. Take
note of the following:
- When linking one service to another, remember to use the container name instead of `localhost`.
- Please set the settings of the -arr containers as soon as possible to the following (use
  advanced):
  - Media management:
    - Use hardlinks instead of Copy: `true`
    - Root folder: `/data/media/` and then tv, movies or music depending on service
- In qBittorrent, after connecting it to the -arr services, you can indicate it should move
  torrents in certain categories to certain directories, like torrents in the `radarr` category
  to `/data/torrents/movies`. You should do this. Also set the `Default Save Path` to
  `/data/torrents`. Set "Run external program on torrent completion" to true and enter this in the
  field: `chmod -R 775 "%F/"`.
- You'll have to add indexers in Prowlarr by hand. Use Prowlarrs settings to connect it to the
  other -arr apps.

## FAQ

### Why do I need to set some settings myself, can that be added?
Some settings, particularly for the Servarr suite, are set in databases. While it *might* be
possible to interact with this database after creation, I'd rather not touch these. It's not
that difficult to set them yourself, and quite difficult to do it automatically. For other
containers, configuration files are automatically generated, so these are more easily edited,
but I currently don't believe this is worth the effort.
