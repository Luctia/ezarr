class ContainerConfig:
    def __init__(self,
                 root_dir,
                 timezone,
                 config_dir=None,
                 plex_claim='',
                 movie_dir=None,
                 tv_dir=None,
                 music_dir=None,
                 book_dir=None,
                 comic_dir=None,
                 torrent_dir=None
                 ):
        self.root_dir = root_dir
        self.timezone = timezone
        self.config_dir = config_dir if config_dir is not None else root_dir + '/config'
        self.plex_claim = plex_claim
        self.movie_dir = movie_dir if movie_dir is not None else root_dir + '/media/movies'
        self.tv_dir = tv_dir if tv_dir is not None else root_dir + '/media/tv'
        self.music_dir = music_dir if music_dir is not None else root_dir + '/media/music'
        self.book_dir = book_dir if book_dir is not None else root_dir + '/media/books'
        self.comic_dir = comic_dir if comic_dir is not None else root_dir + '/media/comics'
        self.torrent_dir = torrent_dir if torrent_dir is not None else root_dir + '/torrents'

    def plex(self):
        return (
            '  plex:\n'
            '    image: lscr.io/linuxserver/plex:latest\n'
            '    container_name: plex\n'
            '    network_mode: host\n'
            '    environment:\n'
            '      - PUID=${UID}\n'
            '      - PGID=13000\n'
            '      - VERSION=docker\n'
            '      - PLEX_CLAIM=' + self.plex_claim + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/plex-config:/config\n'
            '      - ' + self.root_dir + '/data/media:/media\n'
            '    restart: unless-stopped\n'
        )

    def tautulli(self):
        return (
            '  tautulli:\n'
            '    image: lscr.io/linuxserver/tautulli:latest\n'
            '    container_name: tautulli\n'
            '    depends_on:\n'
            '      - plex\n'
            '    environment:\n'
            '      - PUID=${UID}\n'
            '      - PGID=13000\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/tautulli-config:/config\n'
            '    ports:\n'
            '      - 8181:8181\n'
            '    restart: unless-stopped\n'
        )

    def jellyfin(self):
        return (
            '  jellyfin:\n'
            '    image: lscr.io/linuxserver/jellyfin:latest\n'
            '    container_name: jellyfin\n'
            '    environment:\n'
            '      - PUID=${UID}\n'
            '      - PGID=13000\n'
            '      - UMASK=002\n'
            '      - TZ=' + self.timezone + '\n'
            '    volumes:\n'
            '      - ' + self.config_dir + '/jellyfin-config:/config\n'
            '      - ${ROOT_DIR}/data/media:/data\n'
            '    ports:\n'
            '      - 8096:8096\n'
            '    restart: unless-stopped\n'
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
            '      - ${ROOT_DIR}/data:/data\n'
            '    ports:\n'
            '      - 7878:7878\n'
            '    restart: unless-stopped\n'
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
            '      - ${ROOT_DIR}/data:/data\n'
            '    ports:\n'
            '      - 8989:8989\n'
            '    restart: unless-stopped\n'
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
            '      - ${ROOT_DIR}/data:/data\n'
            '    ports:\n'
            '      - 8686:8686\n'
            '    restart: unless-stopped\n'
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
            '      - ${ROOT_DIR}/data:/data\n'
            '    ports:\n'
            '      - 8787:8787\n'
            '    restart: unless-stopped\n'
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
            '      - ${ROOT_DIR}/data:/data\n'
            '    ports:\n'
            '      - 8090:8090\n'
            '    restart: unless-stopped\n'
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
            '      - 9696:9696\n'
            '    restart: unless-stopped\n'
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
            '      - 8080:8080\n'
            '      - 6881:6881\n'
            '      - 6881:6881/udp\n'
            '    restart: unless-stopped\n'
        )
