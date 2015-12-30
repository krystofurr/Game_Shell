from abc import ABCMeta, abstractmethod


class Menu:
    __metaclass__ = ABCMeta

    def __init__(self, db):
        self.db = db

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, event):
        pass

