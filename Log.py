from abc import abstractmethod

class Log():
    @abstractmethod
    def debug(self):
        print()

    @abstractmethod
    def info(self):
        print()

    @abstractmethod
    def warn(self):
        print()

    @abstractmethod
    def error(self):
        print()

    @abstractmethod
    def crit(self):
        print()

class ConsoleLog(Log):
    def debug(self):
        print("\033[32m {}".format("Debug"))

    def info(self):
        print("\033[34m {}".format("Info"))

    def warn(self):
        print("\033[35m {}".format("Warn"))

    def error(self):
        print("\033[31m {}".format("Error"))

    def crit(self):
        print("\033[33m {}".format("Crit"))

asd = ConsoleLog()
asd.debug()
asd.info()
asd.warn()
asd.error()
asd.crit()

