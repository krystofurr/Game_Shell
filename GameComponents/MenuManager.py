import pygame
from Core.GameConfig import GameConfig


class MenuManager:

    # Dictionary to hold all 'Menu' objects
    menuList = {}

    @staticmethod
    def __init__(stateMachine):
        stateMachine = stateMachine

    @staticmethod
    def addMenu(name, menu):
        MenuManager.menuList[name] = menu

    @staticmethod
    def removeMenu(name):
        MenuManager.menuList.pop(name, None)

    '''
        createMenu
        --------------------------------------------------------------------------------
        menuArgs ( Dictionary )
                        {'xPos': None, 'yPos': None, 'containerWidth': None,
                         'optionHeight': None, 'numberOfOptions': None,
                         'mainColor': None, 'selectColor': None, 'thickness': None}

        options ( List ) * Will get converted into a Tuple

        rectContainer ( Rectangle object for main container )
        rectOptions ( Rectangle objects in a list used for the options )

        screen ( Surface )
    '''
    @staticmethod
    def createMenu(menuArgs, options, rectContainer, rectOptions, screen):

        # Draw main container
        pygame.draw.rect(screen, menuArgs['mainColor'], rectContainer, menuArgs['thickness'])

        # Draw each option within the container
        for i in range(menuArgs['numberOfOptions']):
            pygame.draw.rect(screen, menuArgs['mainColor'], rectOptions[i], menuArgs['thickness'])

    '''
        drawText
        ------------------------------------------
        draw some text into an area of a surface
        automatically wraps words
        returns any text that didn't get blitted
        REF: http://pygame.org/wiki/TextWrap
    '''
    @staticmethod
    def drawText(screen, text, color, rect, font, aa=False, bkg=None, center=False):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size(text)[1]
        fontWidth = font.size(text)[0]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            # If 'center' is enabled, center the text
            if center:
                screen.blit(image, (rect.centerx - fontWidth/2, y))
            else:
                screen.blit(image, (rect.left, y))

            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text

    @staticmethod
    def draw(screen):
        # Cycle through all 'Menu' objects and draw
        for name in MenuManager.menuList:
            MenuManager.menuList[name].draw(screen)

    @staticmethod
    def update(event):
        # Cycle through all 'Menu' objects and update
        for name in MenuManager.menuList:
            MenuManager.menuList[name].update(event)


