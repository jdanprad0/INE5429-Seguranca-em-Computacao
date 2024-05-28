import sys


class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")


    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


    def flush(self):
        pass