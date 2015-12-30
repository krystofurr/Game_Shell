from FSM.State import State
from Core.GameConfig import GameConfig
import pygame
from pygame.locals import *


class Settings(State):
    # DOCSTRING
    """ [ Settings State ] This represents the settings or options screen """

    # CONSTRUCTOR
    def __init__(self, stateMachine):
        # Calls 'State' constructor
        State.__init__(self)
        self.stateMachine = stateMachine

    def enter(self):
        print "[ Entering ] Settings"
        # Calls 'State' constructor
        super(Settings, self).enter()

    def execute(self):
        print "[ Executing ] Settings"

    def exit(self):
        print "[ Exiting ] Settings"

    def draw(self, screen):
        fontObj = pygame.font.Font('freesansbold.ttf', 22)
        textSurfaceObj = fontObj.render('Settings State ( Press 2 for TitleScreen )', True, GameConfig.RED)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 150)
        screen.blit(textSurfaceObj, textRectObj)

    def update(self, event):
        print "[ Updating ] Settings"

        # Event Listening
        if event.type == KEYDOWN:
            if event.key == K_2:
                self.stateMachine.toTransition("toTitleScreen")

    # toString
    def __str__(self):
        return self.__doc__
