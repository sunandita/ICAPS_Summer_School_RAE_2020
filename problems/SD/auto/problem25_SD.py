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
rv.EDGES = {1: [2, 4], 2: [1, 3, 5], 3: [2], 4: [1, 5], 5: [2, 4]}
rv.DOORLOCATIONS = {(2, 5): 'd1', (4, 5): 'd2', (1, 2): 'd3', (1, 4): 'd4', (2, 3): 'd5'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1', 'd2', 'd3', 'd4', 'd5']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'ordinary', 'd3': 'spring', 'd4': 'ordinary', 'd5': 'spring'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed', 'd5': 'closed'}
    state.loc = {'r1': 3, 'r2': 2}
    state.pos = {'o1': 2, 'o2': 4}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK, 'd5': UNK}

tasks = {
    1: [['moveTo', 'r1', 1]],
    5: [['moveTo', 'r1', 3]]
}

eventsEnv = {}

