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
rv.EDGES = {1: [2, 3], 2: [1, 5], 3: [1, 4], 4: [3], 5: [2]}
rv.DOORLOCATIONS = {(1, 3): 'd1', (1, 2): 'd2', (3, 4): 'd3', (2, 5): 'd4'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1', 'd2', 'd3', 'd4']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'spring', 'd3': 'spring', 'd4': 'spring'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed'}
    state.loc = {'r1': 1, 'r2': 2}
    state.pos = {'o1': 5, 'o2': 3}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK}

tasks = {
    5: [['fetch', 'r2', 'o2', 1]],
    2: [['moveTo', 'r1', 1]],
    1: [['fetch', 'r2', 'o1', 3]]
}

eventsEnv = {}

