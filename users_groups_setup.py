import os


class UserGroupSetup:
    def __init__(self, root_dir='/'):
        self.root_dir = root_dir
        os.system('sudo groupadd mediacenter -g 13000')

    def sonarr(self):
        os.system('sudo useradd sonarr -u 13001 && sudo mkdir -pv ' + self.root_dir + 'data/{media,torrents}/tv && sudo mkdir -p ' + self.root_dir + 'docker/sonarr-config')
        os.system('sudo usermod -a -G mediacenter sonarr')

    def radarr(self):
        os.system('sudo useradd radarr -u 13002 && sudo mkdir -pv ' + self.root_dir + 'data/{media,torrents}/movies && sudo mkdir -p ' + self.root_dir + 'docker/radarr-config')
        os.system('sudo usermod -a -G mediacenter radarr')

    def lidarr(self):
        os.system('sudo useradd lidarr -u 13003 && sudo mkdir -pv ' + self.root_dir + 'data/{media,torrents}/music && sudo mkdir -p ' + self.root_dir + 'docker/lidarr-config')
        os.system('sudo usermod -a -G mediacenter lidarr')

    def readarr(self):
        os.system('sudo useradd readarr -u 13004 && sudo mkdir -pv ' + self.root_dir + 'data/{media,torrents}/books && sudo mkdir -p ' + self.root_dir + 'docker/readarr-config')
        os.system('sudo usermod -a -G mediacenter readarr')

    def mylar3(self):
        os.system('sudo useradd mylar -u 13005 && sudo mkdir -pv ' + self.root_dir + 'data/{media,torrents}/comics && sudo mkdir -p ' + self.root_dir + 'docker/mylar-config')
        os.system('sudo usermod -a -G mediacenter mylar')

    def prowlarr(self):
        os.system('sudo useradd prowlarr -u 13006 && sudo mkdir -p ' + self.root_dir + 'docker/prowlarr-config')
        os.system('sudo usermod -a -G mediacenter prowlarr')

    def qbittorrent(self):
        os.system('sudo useradd qbittorrent -u 13007')
        os.system('sudo usermod -a -G mediacenter qbittorrent')
