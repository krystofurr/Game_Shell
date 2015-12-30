

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

    @staticmethod
    def draw(screen):
        # Cycle through all 'Menu' objects and draw
        for menu in MenuManager.menuList:
            menu.draw(screen)

    @staticmethod
    def update(event):
        # Cycle through all 'Menu' objects and update
        for name in MenuManager.menuList:
            MenuManager.menuList[name].update(event)




