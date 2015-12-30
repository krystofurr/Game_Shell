from GameComponents.Menu import Menu


class TitleMenu(Menu):

    def __init__(self, db):
        super(TitleMenu, self).__init__(db)

    def update(self, event):
        print 'TITLE MENU UPDATE ++++++++++++++++++++++++'

    def draw(self, screen):
        pass
