'''from configobj import ConfigObj


def get_collector_config(key, value):
    config = configobj.ConfigObj()
    config['server'] = {}
    config['server']['collectors_config_path'] = ''
    config['collectors'] = {}
    config['collectors']['default'] = {}
    config['collectors']['default']['hostname_method'] = "uname_short"
    config['collectors'][key] = value
    return config


#get_collector_config('server', 'bongo')

config = ConfigObj('config.ini')

print(config)
print(config['server']['servername'])
'''


from datetime import datetime

dt = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

print(dt)
