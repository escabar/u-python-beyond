
import os


class ConfigkeyError(Exception):

    def __init__(self, dictinst, key):
        self.keys = dictinst.keys()
        self.key = key

    def __str__(self):
        return '"{0} is not in the config. Available Keys are: ({1})'.format(self.key, self.keys)

class ConfigDict(dict):

    def __init__(self, config_file):
        self._config_file = config_file

        try:
            # if os.path.isfile(self._config_file):
                with open(self._config_file, 'r') as f:
                    for line in f:
                        dict.__setitem__(self, line.split('=')[0], line.split('=')[1].rstrip())
        except IOError:
            raise IOError('sorry nada')

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

        with open(self._config_file, 'w') as f:
            for key, value in self.items():
                f.write(key + "=" + value + "\n")

    def __getitem__(self, key):
        if not key in self:
            raise ConfigkeyError(self, key)
        return dict.__getitem__(self, key)


cd = ConfigDict('config_file.txt')

print(cd['solly'])