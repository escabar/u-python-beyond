
class ConfigDict(dict):

    def __init__(self, config_file):
        self._config_file = config_file

        with open(self._config_file, 'r') as f:
            for line in f:
                dict.__setitem__(self, line.split('=')[0], line.split('=')[1].rstrip())

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

        with open(self._config_file, 'w') as f:
            for key, value in self.items():
                f.write(key + "=" + value + "\n")
