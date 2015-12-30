import sqlite3
from Core.GameConfig import GameConfig


class DB:

    def __init__(self):
        try:
            self.conn = sqlite3.connect(GameConfig.PATH + GameConfig.FILENAME)
            self.cursor = self.conn.cursor()
        except ValueError:
            print 'Could not connect to the database!'

    def getConn(self):
        return self.conn

    def getCursor(self):
        return self.cursor

    def initializeDB(self):
        print 'hi'
        # Create tables

        # Create table attributes



