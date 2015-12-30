"""

 _____                 _   __  __
| ____|_   _____ _ __ | |_|  \/  | __ _ _ __   __ _  __ _  ___ _ __
|  _| \ \ / / _ \ '_ \| __| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |___ \ V /  __/ | | | |_| |  | | (_| | | | | (_| | (_| |  __/ |
|_____| \_/ \___|_| |_|\__|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                                    |___/

Author: Christopher Sigouin
Date: December 27, 2015

"""
from pygame.locals import *
import pygame
from GameComponents.MenuManager import MenuManager


class EventManager(object):

    def __init__(self, stateMachine):

        self.stateMachine = stateMachine

    ''' Any objects that require an event check should be placed here '''
    def run(self):

        for event in pygame.event.get():

            self.stateMachine.curState.update(event)
            MenuManager.update(event)

            if event.type == QUIT:
                exit()


