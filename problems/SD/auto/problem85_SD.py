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

rv.LOCATIONS = [1, 2, 3, 4, 5, 6, 7, 8]
rv.EDGES = {1: [2, 5], 2: [1, 3, 4], 3: [2, 6], 4: [2, 5, 6], 5: [1, 4], 6: [4, 3, 7], 7: [6, 8], 8: [7]}
rv.DOORLOCATIONS = {(7, 8): 'd1', (2, 4): 'd2', (4, 5): 'd3', (1, 2): 'd4', (3, 6): 'd5'}
rv.ROBOTS = ['r1', 'r2', 'r3']
rv.DOORS = ['d1', 'd2', 'd3', 'd4', 'd5']
rv.DOORTYPES = {'d1': 'ordinary', 'd2': 'ordinary', 'd3': 'spring', 'd4': 'spring', 'd5': 'spring'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed', 'd5': 'closed'}
    state.loc = {'r1': 4, 'r2': 6, 'r3': 7}
    state.pos = {'o1': 3, 'o2': 4, 'o3': 8}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK, 'd5': UNK}

tasks = {
    3: [['moveTo', 'r2', 6]],
    1: [['fetch', 'r1', 'o3', 8]],
    4: [['fetch', 'r2', 'o2', 6]]
}

eventsEnv = {}

