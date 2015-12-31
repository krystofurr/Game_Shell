"""

 ____  _           _             __  __
|  _ \(_)___ _ __ | | __ _ _   _|  \/  | __ _ _ __   __ _  __ _  ___ _ __
| | | | / __| '_ \| |/ _` | | | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_| | \__ \ |_) | | (_| | |_| | |  | | (_| | | | | (_| | (_| |  __/ |
|____/|_|___/ .__/|_|\__,_|\__, |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
            |_|            |___/                          |___/

Author: Christopher Sigouin
Date: December 27, 2015

"""
from Core.GameConfig import GameConfig
import pygame

from GameComponents.MenuManager import MenuManager


class DisplayManager(object):

    def __init__(self, stateMachine):

        self.stateMachine = stateMachine
        pygame.display.set_caption(GameConfig.GAME_TITLE)
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT),
                                              GameConfig.SCREEN_CONFIG, GameConfig.SCREEN_COLOR_DEPTH)

    ''' Any objects that require drawing should be placed here '''
    def run(self):
        # Clear the screen before drawing
        self.screen.fill(GameConfig.SCREEN_CLEAR_COLOR)
        # Draw the current state
        self.stateMachine.curState.draw(self.screen)

        MenuManager.draw(self.screen)

        # Update the display
        pygame.display.update()
