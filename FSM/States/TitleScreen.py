from FSM.State import State
from Core.GameConfig import GameConfig
import pygame
from pygame.locals import *
from GameComponents.MenuManager import MenuManager
from GameComponents.TitleMenu import TitleMenu


class TitleScreen(State):
    # DOCSTRING
    """ [ TitleScreen State ] This is the title screen to start the game """

    # CONSTRUCTOR
    def __init__(self, stateMachine, db):
        # Calls 'State' constructor
        State.__init__(self)
        self.stateMachine = stateMachine

        # Create 'TitleMenu' for this state and add to the 'MenuManager'
        MenuManager.addMenu("TitleMenu", TitleMenu(db))

    def enter(self):
        print "[ Entering ] TitleScreen"
        # Calls 'State' constructor
        super(TitleScreen, self).enter()

    def execute(self):
        print "[ Executing ] TitleScreen"

    def exit(self):
        print "[ Exiting ] TitleScreen"

    def draw(self, screen):
        fontObj = pygame.font.Font(None, GameConfig.FONT_SIZE_TITLE)
        textSurfaceObj = fontObj.render('TitleScreen State ( Press 1 for InGame )', True, GameConfig.WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (GameConfig.SCREEN_WIDTH / 2, 150)
        screen.blit(textSurfaceObj, textRectObj)

    def update(self, event):
        print "[ Updating ] TitleScreen"

        # Event Listening
        if event.type == KEYDOWN:
            if event.key == K_1:
                self.stateMachine.toTransition("toInGame")

    # toString
    def __str__(self):
        return self.__doc__

