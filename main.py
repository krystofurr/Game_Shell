"""
 __  __       _
|  \/  | __ _(_)_ __
| |\/| |/ _` | | '_ \
| |  | | (_| | | | | |
|_|  |_|\__,_|_|_| |_|

This file represents the main executable file for the SimpleGameEngine

"""
import sys
import pygame
from Core.GameConfig import GameConfig
from Core.GameEngine import GameEngine
from Util.DB import DB

if __name__ == '__main__':

    # Initialize database
    db = DB()

    # Create an instance of the engine
    gameEngine = GameEngine(db)

    clock = pygame.time.Clock()
    '''
        GAME LOOP ( Handle Events, Update Game State, Draw Screen )
    '''
    while True:

        gameEngine.execute()
        clock.tick(GameConfig.FPS)
