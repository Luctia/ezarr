# EZARR
Ezarr is a project built to make it EZ to deploy a Servarr mediacenter, featuring:
- Sonarr
- Radarr
- Lidarr
- Prowlarr
- qBittorrent
- PleX

## Using
1. To get started, clone the repository in a directory of your choosing.
2. Copy `.env.sample` to a real `.env`: `$ cp .env.sample .env`.
3. Set the environment variables to your liking.
4. Run `setup.sh` as superuser. This will set up your users, a system of directories, ensure
   permissions are set correctly and sets some more environment variables for docker compose.
5. Run `docker compose up`

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
  to `/data/torrents/movies`. You should do this.
- You'll have to add indexers in Prowlarr by hand. Use Prowlarrs settings to connect it to the
  other -arr apps.
