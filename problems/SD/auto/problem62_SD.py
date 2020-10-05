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

rv.LOCATIONS = [1, 2, 3, 4, 5, 6, 7]
rv.EDGES = {1: [2], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5], 5: [2, 4, 6], 6: [5, 7], 7: [6]}
rv.DOORLOCATIONS = {(6, 7): 'd1', (2, 3): 'd2', (1, 2): 'd3', (2, 5): 'd4', (4, 5): 'd5'}
rv.ROBOTS = ['r1', 'r2', 'r3']
rv.DOORS = ['d1', 'd2', 'd3', 'd4', 'd5']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'ordinary', 'd3': 'spring', 'd4': 'spring', 'd5': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed', 'd5': 'closed'}
    state.loc = {'r1': 3, 'r2': 6, 'r3': 5}
    state.pos = {'o1': 7, 'o2': 4, 'o3': 6}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK, 'd5': UNK}

tasks = {
    1: [['fetch', 'r2', 'o1', 1]],
    2: [['moveTo', 'r3', 2]]
}

eventsEnv = {}

