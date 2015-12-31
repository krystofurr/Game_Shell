import pygame
from Core.GameConfig import GameConfig
from GameComponents.Menu import Menu
from GameComponents.MenuManager import MenuManager


class TitleMenu(Menu):

    def __init__(self, db):
        super(TitleMenu, self).__init__(db)

        # Menu arguments for the 'TitleMenu'
        self.menuArgs['containerWidth'] = 200
        self.menuArgs['optionHeight'] = 30
        self.menuArgs['numberOfOptions'] = 3
        self.menuArgs['mainColor'] = GameConfig.RED
        self.menuArgs['selectColor'] = 100
        self.menuArgs['thickness'] = 3
        self.menuArgs['xPos'] = GameConfig.SCREEN_WIDTH / 2 - self.menuArgs['containerWidth'] / 2
        self.menuArgs['yPos'] = 350

        # Initialize the menu upon creation
        self.initializeMenu()

    '''
        initializeMenu - Helper function to initialize
    '''
    def initializeMenu(self):
        # Options for the 'TitleMenu'
        self.options = ('New Game', 'Load Game', 'Exit')
        # List to add the rect option objects
        self.rectOptions = []
        # Offset for displaying each option
        optionOffset = 0

        # Create the main container
        self.rectContainer = pygame.Rect(self.menuArgs['xPos'], self.menuArgs['yPos'], self.menuArgs['containerWidth'],
                                        (self.menuArgs['optionHeight'] * self.menuArgs['numberOfOptions']))

        # Create an option container and add it to 'rectOptions'
        for i in range(self.menuArgs['numberOfOptions']):
            self.rectOptions.append(pygame.Rect(self.menuArgs['xPos'], self.menuArgs['yPos'] + optionOffset,
                                                self.menuArgs['containerWidth'],
                                                self.menuArgs['optionHeight']))

            optionOffset += self.menuArgs['optionHeight']

        # Change the options list to a tuple
        self.rectOptions = tuple(self.rectOptions)

    def update(self, event):
        print 'TITLE MENU UPDATE ++++++++++++++++++++++++'

    def draw(self, screen):

        # Draw the menu
        MenuManager.createMenu(self.menuArgs, self.options, self.rectContainer, self.rectOptions, screen)

        # Draw the text inside the menu
        for i in range(self.menuArgs['numberOfOptions']):
            MenuManager.drawText(screen, self.options[i], GameConfig.WHITE, self.rectOptions[i], self.font, center=True)
