from abc import ABCMeta, abstractmethod


class State:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def update(self, event):
        pass

    @abstractmethod
    def draw(self, screen):
        pass




