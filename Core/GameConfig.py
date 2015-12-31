"""

  ____                       ____             __ _
 / ___| __ _ _ __ ___   ___ / ___|___  _ __  / _(_) __ _
| |  _ / _` | '_ ` _ \ / _ \ |   / _ \| '_ \| |_| |/ _` |
| |_| | (_| | | | | | |  __/ |__| (_) | | | |  _| | (_| |
 \____|\__,_|_| |_| |_|\___|\____\___/|_| |_|_| |_|\__, |
                                                   |___/


"""


class GameConfig:

    def __init__(self):
        pass

    # Drawing properties
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    # Text properties
    FONT_SIZE_MENU = 25
    FONT_SIZE_TITLE = 35

    # Screen properties
    FPS = 60
    GAME_TITLE = "My Game Title"
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SCREEN_CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    SCREEN_CONFIG = 0
    SCREEN_COLOR_DEPTH = 32
    SCREEN_CLEAR_COLOR = BLACK

    # Database
    PATH = './resources/'
    FILENAME = 'game.db'


