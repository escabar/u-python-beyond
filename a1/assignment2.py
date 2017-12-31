import abc
from datetime import datetime


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, msg):

        with open(self.filename, 'a') as f:
            f.write(msg + '\n')


class LogFile(WriteFile):

    def write(self, msg):
        self.write_to_file(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' ' + msg)


class DelimFile(WriteFile):

    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, alist):
        self.write_to_file(self.delim.join(alist))




