__author__ = 'patras'

from domain_springDoor import *
from timer import DURATION
from state import state

DURATION.TIME = {
    'unlatch1': 5,
    'unlatch2': 5,
    'holdDoor': 2,
    'passDoor': 3,
    'releaseDoor': 2,
    'closeDoors': 3,
    'move': 10,
    'take': 2,
    'put': 2,
}

DURATION.COUNTER = {
    'unlatch1': 5,
    'unlatch2': 5,
    'holdDoor': 2,
    'passDoor': 3,
    'releaseDoor': 2,
    'closeDoors': 3,
    'move': 10,
    'take': 2,
    'put': 2,
}

rv.LOCATIONS = [1, 2, 3, 4]
rv.EDGES = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
rv.DOORLOCATIONS = {(2, 4): 'd1'}
rv.ROBOTS = ['r1', 'r2', 'r3']
rv.DOORS = ['d1']
rv.DOORTYPES = {'d1': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}
    state.doorStatus = {'d1': 'closed'}
    state.loc = {'r1': 2, 'r2': 1, 'r3': 1}
    state.pos = {'o1': 3, 'o2': 1, 'o3': 1}
    state.done = {0: False}
    state.doorType = {'d1': UNK}

tasks = {
    2: [['moveTo', 'r3', 1]],
    3: [['moveTo', 'r3', 1]]
}

eventsEnv = {}

