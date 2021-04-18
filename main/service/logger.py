from abc import abstractmethod

class Logger():

    @abstractmethod
    def append(self, message):
        pass
    