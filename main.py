from container_configs import ContainerConfig
from users_groups_setup import UserGroupSetup

services_classed = dict()


def take_input(service_name, service_type):
    choice = input()
    if choice == 'Y' or choice == 'y' or choice == '':
        services_classed[service_type].append(service_name)
    elif choice != 'n' and choice != 'N':
        print('Invalid input, please enter Y or N. Not adding ' + service_name + ".")


def take_boolean_input(default=True):
    while True:
        ans = input()
        if ans == '':
            return default
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False
        print('Please answer with y or n.', end=' ')


def take_directory_input():
    while True:
        ans = input()
        if ans[0] == '/':
            if ans[-1] == '/':
                return ans[:-1]
            return ans
        print('Please make sure the path is absolute, meaning it starts at the root of your filesystem and starts with "/":', end=' ')


print('Welcome to the EZarr CLI.')
print('This CLI will ask you which services you\'d like to use and more. If you\'d like more information about a '
      'certain service, look in the README.')

print('\n===SERVARR===')
services_classed['servarr'] = []
print('Use Sonarr? [Y/n]', end=" ")
take_input('sonarr', 'servarr')
print('Use Radarr? [Y/n]', end=" ")
take_input('radarr', 'servarr')
print('Use Lidarr? [Y/n]', end=" ")
take_input('lidarr', 'servarr')
print('Use Readarr? [Y/n]', end=" ")
take_input('readarr', 'servarr')
print('Use Mylar3? [Y/n]', end=" ")
take_input('mylar3', 'servarr')
print('Use Audiobookshelf? [Y/n]', end=" ")
take_input('audiobookshelf', 'servarr')
if len(services_classed['servarr']) == 0:
    print('Warning: no media management services selected.')
if services_classed['servarr'].__contains__('sonarr') or services_classed['servarr'].__contains__('radarr'):
    print('Use Bazarr? [Y/n]', end=" ")
    take_input('bazarr', 'servarr')

print('\n===INDEXERS===')
services_classed['indexer'] = []
print('Use Prowlarr? [Y/n]', end=" ")
take_input('prowlarr', 'indexer')
if len(services_classed['indexer']) == 0:
    print('Warning: no indexing service selected.')

print('\n===MEDIA SERVERS===')
services_classed['ms'] = []
print('Use PleX? [Y/n]', end=" ")
take_input('plex', 'ms')
if services_classed['ms'].__contains__('plex'):
    print('Use Tautulli? [Y/n]', end=" ")
    take_input('tautulli', 'ms')
    if services_classed['servarr'].__contains__('sonarr') or services_classed['servarr'].__contains__('radarr'):
        print('Use Overseerr? [Y/n]', end=" ")
        take_input('overseerr', 'servarr')
print('Use Jellyfin? [Y/n]', end=" ")
take_input('jellyfin', 'ms')
if (services_classed['ms'].__contains__('jellyfin')
        and (services_classed['servarr'].__contains__('sonarr') or services_classed['servarr'].__contains__('radarr'))):
    print('Use Jellyseerr? [Y/n]', end=" ")
    take_input('jellyseerr', 'servarr')
if len(services_classed['ms']) == 0:
    print('Warning: no media servers selected.')

print('\n===BITTORRENT===')
services_classed['torrent'] = []
print('Use qBittorrent? [Y/n]', end=" ")
take_input('qbittorrent', 'torrent')

print('\n===USENET===')
services_classed['usenet'] = []
print('Use SABnzbd? [Y/n]', end=" ")
take_input('sabnzbd', 'usenet')

if len(services_classed['torrent']) == 0 and len(services_classed['usenet']) == 0:
    print('Warning: no usenet or BitTorrent clients selected.')

services = []
for service_class in services_classed.keys():
    services.extend(services_classed[service_class])
if len(services) == 0:
    print('No services selected. Terminating.')
    exit(1)

print('\n===CONFIGURATION===')
print('Please enter your timezone (like "Europe/Amsterdam")', end=' ')
timezone = input()
if len(timezone) == 0:
    timezone = 'Europe/Amsterdam'
plex_claim = ''
if services.__contains__('plex'):
    print('If you have a PleX claim token, enter it now. Otherwise, just press enter.', end=' ')
    plex_claim = input()

print('Where would you like to keep your files?', end=' ')
root_dir = take_directory_input()

compose = open('docker-compose.yml', 'w')
compose.write(
    '---\n'
    'version: "3.1"\n'
    'services:\n'
)

container_config = ContainerConfig(root_dir, timezone, plex_claim=plex_claim)
permission_setup = UserGroupSetup(root_dir=root_dir)

for service in services:
    try:
        getattr(permission_setup, service)()
    except AttributeError:
        pass
    compose.write(getattr(container_config, service)())
compose.close()

print('Process complete. You can now run "docker compose up -d" to start your containers.')
print('Thank you for using EZarr. If you experience any issues or have feature requests, add them to our issues.')
print('For questions, you can also use the discussions tab.')
exit(0)
