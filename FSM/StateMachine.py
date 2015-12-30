"""
 ____  _        _       __  __            _     _
/ ___|| |_ __ _| |_ ___|  \/  | __ _  ___| |__ (_)_ __   ___
\___ \| __/ _` | __/ _ \ |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
 ___) | || (_| | ||  __/ |  | | (_| | (__| | | | | | | |  __/
|____/ \__\__,_|\__\___|_|  |_|\__,_|\___|_| |_|_|_| |_|\___|

Author: Christopher Sigouin
Date: December 27, 2015

REF: https://www.youtube.com/watch?v=E45v2dD3IQU

"""


class StateMachine:

    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None

    def addTransition(self, transName, transition):
        self.transitions[transName] = transition

    def addState(self, stateName, state):
        self.states[stateName] = state

    def setState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def toTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    ''' IN LOOP '''
    def execute(self):
        if(self.trans):
            self.curState.exit()
            self.trans.execute()
            self.setState(self.trans.toState)
            self.curState.enter()
            self.trans = None
        self.curState.execute()

