from abc import ABCMeta, abstractmethod

import pygame

from Core.GameConfig import GameConfig


class Menu:
    __metaclass__ = ABCMeta

    def __init__(self, db):
        self.db = db
        # Menu dictionary for the 'createMenu' method of MenuManager
        self.menuArgs = {'xPos': None, 'yPos': None, 'containerWidth': None,
                         'optionHeight': None, 'numberOfOptions': None,
                         'mainColor': None, 'selectColor': None, 'thickness': None}
        # Options for the menu.  Use a 'Tuple'
        self.options = None
        # Rectangle object for the main container of the menu
        self.rectContainer = None
        # Rectangle objects for each menu option
        self.rectOptions = None
        # Font object for displaying text inside menus
        self.font = pygame.font.Font(None, GameConfig.FONT_SIZE_MENU)

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, event):
        pass


