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
rv.EDGES = {1: [2], 2: [1, 3, 4], 3: [2], 4: [2]}
rv.DOORLOCATIONS = {(2, 3): 'd1'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1']
rv.DOORTYPES = {'d1': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed'}
    state.loc = {'r1': 1, 'r2': 1}
    state.pos = {'o1': 2, 'o2': 4}
    state.done = {0: False}
    state.doorType = {'d1': UNK}

tasks = {
    1: [['moveTo', 'r1', 1]],
    5: [['moveTo', 'r2', 2]],
    3: [['moveTo', 'r1', 4]]
}

eventsEnv = {}

