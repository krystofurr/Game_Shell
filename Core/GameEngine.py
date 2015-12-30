import pygame

import sqlite3

from FSM.StateMachine import StateMachine
from FSM.States.InGame import InGame
from FSM.States.Settings import Settings
from FSM.States.TitleScreen import TitleScreen
from FSM.Transition import Transition
from GameComponents.MenuManager import MenuManager
from GameMechanics.DisplayManager import DisplayManager
from GameMechanics.EventManager import EventManager
from Util.DB import DB


class GameEngine(object):

    def __init__(self, db):

        # Initialize PyGame
        pygame.init()

        self.stateMachine = StateMachine()

        # States
        self.stateMachine.addState("TitleScreen", TitleScreen(self.stateMachine, db))
        self.stateMachine.addState("Settings", Settings(self.stateMachine))
        self.stateMachine.addState("InGame", InGame(self.stateMachine))
        # Transitions
        self.stateMachine.addTransition("toTitleScreen", Transition("TitleScreen"))
        self.stateMachine.addTransition("toSettings", Transition("Settings"))
        self.stateMachine.addTransition("toInGame", Transition("InGame"))

        # Set the initial state
        self.stateMachine.setState("TitleScreen")

        # Initialize Managers
        self.eventManager = EventManager(self.stateMachine)
        self.displayManager = DisplayManager(self.stateMachine)
        self.menuManager = MenuManager(self.stateMachine)

    # ( Handle Events, Update Game State, Draw Screen )
    def execute(self):
        # Handle events
        self.eventManager.run()
        self.stateMachine.execute()
        self.displayManager.run()
