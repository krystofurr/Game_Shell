import pygame
from pygame.locals import *
from Core.GameConfig import GameConfig
from FSM.State import State


class InGame(State):
    # DOCSTRING
    """ [ Game State ] This is the main state of the game """

    # CONSTRUCTOR
    def __init__(self, stateMachine):
        # Calls 'State' constructor
        State.__init__(self)
        self.stateMachine = stateMachine

    def enter(self):
        print "[ Entering ] InGame"
        # Calls 'State' constructor
        super(InGame, self).enter()

    def execute(self):
        print "[ Executing ] InGame"

    def exit(self):
        print "[ Exiting ] InGame"

    def draw(self, screen):
        fontObj = pygame.font.Font('freesansbold.ttf', 22)
        textSurfaceObj = fontObj.render('InGame State ( Press 3 for Settings )', True, GameConfig.YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 150)
        screen.blit(textSurfaceObj, textRectObj)

    def update(self, event):
        print "[ Updating ] InGame"

        # Event Listening
        if event.type == KEYDOWN:
            if event.key == K_3:
                self.stateMachine.toTransition("toSettings")

    # toString
    def __str__(self):
        return self.__doc__
