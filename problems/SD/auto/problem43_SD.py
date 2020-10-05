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
rv.EDGES = {1: [2, 3], 2: [1, 4], 3: [1, 7], 4: [2, 5], 5: [4, 6], 6: [5], 7: [3]}
rv.DOORLOCATIONS = {(1, 2): 'd1', (2, 4): 'd2', (1, 3): 'd3', (4, 5): 'd4'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1', 'd2', 'd3', 'd4']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'spring', 'd3': 'spring', 'd4': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed'}
    state.loc = {'r1': 4, 'r2': 2}
    state.pos = {'o1': 7, 'o2': 6}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK}

tasks = {
    4: [['fetch', 'r2', 'o1', 2]],
    3: [['fetch', 'r1', 'o2', 3]]
}

eventsEnv = {}

