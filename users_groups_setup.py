import os


class UserGroupSetup:
    def __init__(self, root_dir='/'):
        self.root_dir = root_dir
        os.system('sudo groupadd mediacenter -g 13000')

    def create_config_dir(self, service_name):
        os.system(
            f'sudo mkdir -p {self.root_dir}/docker/{service_name}-config'
            f' && sudo chown -R {service_name}:mediacenter {self.root_dir}/docker/{service_name}-config'
        )

    def sonarr(self):
        os.system(
            'sudo useradd sonarr -u 13001'
            ' && sudo mkdir -pv ' + self.root_dir + '/data/{media,torrents}/tv -m 775'
        )
        self.create_config_dir('sonarr')
        os.system('sudo usermod -a -G mediacenter sonarr')

    def radarr(self):
        os.system(
            'sudo useradd radarr -u 13002'
            ' && sudo mkdir -pv ' + self.root_dir + '/data/{media,torrents}/movies -m 775'
        )
        self.create_config_dir('radarr')
        os.system('sudo usermod -a -G mediacenter radarr')

    def lidarr(self):
        os.system(
            'sudo useradd lidarr -u 13003'
            ' && sudo mkdir -pv ' + self.root_dir + '/data/{media,torrents}/music -m 775'
        )
        self.create_config_dir('lidarr')
        os.system('sudo usermod -a -G mediacenter lidarr')

    def readarr(self):
        os.system(
            'sudo useradd readarr -u 13004'
            ' && sudo mkdir -pv ' + self.root_dir + '/data/{media,torrents}/books -m 775'
        )
        self.create_config_dir('readarr')
        os.system('sudo usermod -a -G mediacenter readarr')

    def mylar3(self):
        os.system(
            'sudo useradd mylar -u 13005'
            ' && sudo mkdir -pv ' + self.root_dir + '/data/{media,torrents}/comics -m 775'
        )
        self.create_config_dir('mylar')
        os.system('sudo usermod -a -G mediacenter mylar')

    def audiobookshelf(self):
        os.system(
            'sudo useradd audiobookshelf -u 13009'
            ' && sudo mkdir -pv ' + self.root_dir + '/data/{media,torrents}/audiobooks -m 775'
        )
        self.create_config_dir('audiobookshelf')
        os.system('sudo usermod -a -G mediacenter audiobookshelf')

    def prowlarr(self):
        os.system('sudo useradd prowlarr -u 13006')
        self.create_config_dir('prowlarr')
        os.system('sudo usermod -a -G mediacenter prowlarr')

    def qbittorrent(self):
        os.system('sudo useradd qbittorrent -u 13007')
        os.system('sudo usermod -a -G mediacenter qbittorrent')
