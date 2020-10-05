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

rv.LOCATIONS = [1, 2, 3, 4, 5]
rv.EDGES = {1: [2, 4], 2: [1, 3], 3: [2, 5], 4: [1], 5: [3]}
rv.DOORLOCATIONS = {(1, 4): 'd1', (2, 3): 'd2', (1, 2): 'd3', (3, 5): 'd4'}
rv.ROBOTS = ['r1', 'r2', 'r3']
rv.DOORS = ['d1', 'd2', 'd3', 'd4']
rv.DOORTYPES = {'d1': 'ordinary', 'd2': 'spring', 'd3': 'spring', 'd4': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed'}
    state.loc = {'r1': 1, 'r2': 2, 'r3': 3}
    state.pos = {'o1': 3, 'o2': 5, 'o3': 2}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK}

tasks = {
    2: [['moveTo', 'r3', 3]]
}

eventsEnv = {}

