import os 

class ContainerConfig:
    def __init__(self,
                 root_dir,
                 timezone,
                 plex_claim='',
                 ):
        self.root_dir = root_dir
        self.timezone = timezone
        self.config_dir = root_dir + '/config'
        self.plex_claim = plex_claim
        self.movie_dir = root_dir + '/media/movies'
        self.tv_dir = root_dir + '/media/tv'
        self.music_dir = root_dir + '/media/music'
        self.book_dir = root_dir + '/media/books'
        self.comic_dir = root_dir + '/media/comics'
        self.torrent_dir = root_dir + '/data/torrents'
        self.usenet_dir = root_dir + '/data/usenet'
        self.homarr_dir = root_dir + '/data/homarr/appdata'
        self.UID = os.popen('id -u').read().rstrip('\n')

    def plex(self):
        return (
            '  plex:\n'
            '    image: lscr.io/linuxserver/plex:latest\n'
            '    container_name: plex\n'
            '    network_mode: host\n'
            '    environment:\n'
            '      - PUID=13010\n'
            '      - PGID=13000\n'
            '      - VERSION=docker\n'
            '      - PLEX_CLAIM=' + self.plex_claim + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/plex-config:/config\n'
            '      - ' + self.root_dir + '/data/media:/media\n'
            '    restart: unless-stopped\n\n'
        )

    def tautulli(self):
        return (
            '  tautulli:\n'
            '    image: lscr.io/linuxserver/tautulli:latest\n'
            '    container_name: tautulli\n'
            '    depends_on:\n'
            '      - plex\n'
            '    environment:\n'
            '      - PUID='+ self.UID + '\n'
            '      - PGID=13000\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/tautulli-config:/config\n'
            '    ports:\n'
            '      - "8181:8181"\n'
            '    restart: unless-stopped\n\n'
        )

    def jellyfin(self):
        return (
            '  jellyfin:\n'
            '    image: lscr.io/linuxserver/jellyfin:latest\n'
            '    container_name: jellyfin\n'
            '    environment:\n'
            '      - PUID='+ self.UID + '\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/jellyfin-config:/config\n'
            '      - ' + self.root_dir + '/data/media:/data\n'
            '    ports:\n'
            '      - "8096:8096"\n'
            '    restart: unless-stopped\n\n'
        )

    def sonarr(self):
        return (
            '  sonarr:\n'
            '    image: lscr.io/linuxserver/sonarr:latest\n'
            '    container_name: sonarr\n'
            '    environment:\n'
            '      - PUID=13001\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/sonarr-config:/config\n'
            '      - ' + self.root_dir + '/data:/data\n'
            '    ports:\n'
            '      - "8989:8989"\n'
            '    restart: unless-stopped\n\n'
        )

    def radarr(self):
        return (
            '  radarr:\n'
            '    image: lscr.io/linuxserver/radarr:latest\n'
            '    container_name: radarr\n'
            '    environment:\n'
            '      - PUID=13002\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/radarr-config:/config\n'
            '      - ' + self.root_dir + '/data:/data\n'
            '    ports:\n'
            '      - "7878:7878"\n'
            '    restart: unless-stopped\n\n'
        )

    def bazarr(self):
        return (
            '  bazarr:\n'
            '    image: lscr.io/linuxserver/bazarr:latest\n'
            '    container_name: bazarr\n'
            '    environment:\n'
            '      - PUID=13013\n'
            '      - PGID=13000\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/bazarr-config:/config\n'
            '      - ' + self.root_dir + '/data/media:/media\n'
            '    ports:\n'
            '      - "6767:6767"\n'
            '    restart: unless-stopped\n\n'
        )

    def lidarr(self):
        return (
            '  lidarr:\n'
            '    image: lscr.io/linuxserver/lidarr:latest\n'
            '    container_name: lidarr\n'
            '    environment:\n'
            '      - PUID=13003\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/lidarr-config:/config\n'
            '      - ' + self.root_dir + '/data:/data\n'
            '    ports:\n'
            '      - "8686:8686"\n'
            '    restart: unless-stopped\n\n'
        )

    def readarr(self):
        return (
            '  readarr:\n'
            '    image: lscr.io/linuxserver/readarr:develop\n'
            '    container_name: readarr\n'
            '    environment:\n'
            '      - PUID=13004\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/readarr-config:/config\n'
            '      - ' + self.root_dir + '/data:/data\n'
            '    ports:\n'
            '      - "8787:8787"\n'
            '    restart: unless-stopped\n\n'
        )

    def mylar3(self):
        return (
            '  mylar3:\n'
            '    image: lscr.io/linuxserver/mylar3:latest\n'
            '    container_name: mylar3\n'
            '    environment:\n'
            '      - PUID=13005\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/mylar-config:/config\n'
            '      - ' + self.root_dir + '/data:/data\n'
            '    ports:\n'
            '      - "8090:8090"\n'
            '    restart: unless-stopped\n\n'
        )

    def audiobookshelf(self):
        return (
            '  audiobookshelf:\n'
            '    image: ghcr.io/advplyr/audiobookshelf:latest\n'
            '    container_name: audiobookshelf\n'
            '    environment:\n'
            '      - user=13014:13000\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/audiobookshelf:/config\n'
            '      - ' + self.root_dir + '/data/media/audiobooks:/audiobooks\n'
            '      - ' + self.root_dir + '/data/media/podcasts:/podcasts\n'
            '      - ' + self.root_dir + '/data/media/audiobookshelf-metadata:/metadata\n'
            '    ports:\n'
            '      - "13378:80"\n'
            '    restart: unless-stopped\n\n'
        )

    def prowlarr(self):
        return (
            '  prowlarr:\n'
            '    image: lscr.io/linuxserver/prowlarr:develop\n'
            '    container_name: prowlarr\n'
            '    environment:\n'
            '      - PUID=13006\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/prowlarr-config:/config\n'
            '    ports:\n'
            '      - "9696:9696"\n'
            '    restart: unless-stopped\n\n'
        )

    def homarr(self):
        key = os.urandom(32).hex()  # Because os.urandom(32) generates 32 random bytes, and .hex() converts each byte into two hexadecimal characters.
        return (
            '  homarr:\n'
            '    image: ghcr.io/homarr-labs/homarr:latest\n'
            '    container_name: homarr\n'
            '    environment:\n'
            '      - SECRET_ENCRYPTION_KEY=' + key + '\n'
            '    volumes:\n'
            '      - ' + self.homarr_dir + ':/appdata\n'
            '      - /var/run/docker.sock:/var/run/docker.sock\n'
            '    ports:\n'
            '      - "7575:7575"\n'
            '    restart: unless-stopped\n\n'
        )

    def qbittorrent(self):
        return (
            '  qbittorrent:\n'
            '    image: lscr.io/linuxserver/qbittorrent:latest\n'
            '    container_name: qbittorrent\n'
            '    environment:\n'
            '      - PUID=13007\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '      - WEBUI_PORT=8080\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/qbittorrent-config:/config\n'
            '      - ' + self.torrent_dir + ':/data/torrents\n'
            '    ports:\n'
            '      - "8080:8080"\n'
            '      - "6881:6881"\n'
            '      - "6881:6881/udp"\n'
            '    restart: unless-stopped\n\n'
        )

    def overseerr(self):
        return (
            '  overseerr:\n'
            '    image: sctx/overseerr:latest\n'
            '    container_name: overseerr\n'
            '    environment:\n'
            '      - PUID=13009\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/overseerr-config:/app/config\n'
            '    ports:\n'
            '      - "5055:5055"\n'
            '    restart: unless-stopped\n\n'
        )
    
    def jellyseerr(self):
        return (
            '  jellyseerr:\n'
            '    image: fallenbagel/jellyseerr:latest\n'
            '    container_name: jellyseerr\n'
            '    environment:\n'
            '      - PUID=13012\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/jellyseerr-config:/app/config\n'
            '    ports:\n'
            '      - "5056:5055"\n'
            '    restart: unless-stopped\n\n'
        )

    def sabnzbd(self):
        return (
            '  sabnzbd:\n'
            '    image: lscr.io/linuxserver/sabnzbd:latest\n'
            '    container_name: sabnzbd\n'
            '    environment:\n'
            '      - PUID=13011\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/sabnzbd-config:/config\n'
            '      - ' + self.usenet_dir + ':/data/usenet\n'
            '    ports:\n'
            '      - "8081:8080"\n'
            '    restart: unless-stopped\n\n'
        )
    
    def jackett(self):
        return (
            '  jackett:\n'
            '    image: lscr.io/linuxserver/jackett:latest\n'
            '    container_name: jackett\n'
            '    environment:\n'
            '      - PUID=13008\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/jackett-config:/config\n'
            '    ports:\n'
            '      - 9117:9117\n'
            '    restart: unless-stopped\n\n'
        )
    
    def flaresolverr(self):
        return (
            '  flaresolverr:\n'
            '    image: ghcr.io/flaresolverr/flaresolverr:latest\n'
            '    container_name: flaresolverr\n'
            '    environment:\n'
            '      - LOG_LEVEL=${LOG_LEVEL:-info}\n'
            '      - LOG_HTML=${LOG_HTML:-false}\n'
            '      - CAPTCHA_SOLVER=${CAPTCHA_SOLVER:-none}\n'
            '      - TZ=' + self.timezone + '\n'
            '    ports:\n'
            '      - "8191:8191"\n'
            '    restart: unless-stopped\n\n'
        )
        
