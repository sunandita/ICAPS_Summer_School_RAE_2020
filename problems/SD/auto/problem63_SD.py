__author__ = 'patras'

from domain_springDoor import *
from timer import DURATION
from state import state, rv

DURATION.TIME = {
    'unlatch1': 5,
    'unlatch2': 5,
    'holdDoor': 2,
    'passDoor': 3,
    'releaseDoor': 2,
    'closeDoors': 3,
    'move': 7,
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
    'move': 7,
    'take': 2,
    'put': 2,
}

rv.LOCATIONS = [1, 2, 3, 4, 5, 6]
rv.EDGES = {1: [4], 2: [5], 3: [6], 4: [1, 5], 5: [2, 4, 6], 6: [3, 5]}
rv.DOORS = ['d1', 'd2', 'd3']
rv.DOORLOCATIONS = {(1, 4): 'd3', (2, 5): 'd2', (3, 6): 'd1'}
rv.DOORTYPES = {'d1': 'ordinary', 'd2': 'spring', 'd3': 'spring'}
rv.ROBOTS = ['r1', 'r2', 'r3', 'r4']

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL}
    state.status = {'r1': 'free', 'r2': 'free', 'r3': 'free', 'r4': 'free'}
    state.loc = {'r1': 4, 'r2': 6, 'r3': 6, 'r4': 1}
    state.pos = {'o1': 4}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', }
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, }

tasks = {
    9: [['fetch', 'r1', 'o1', 2]],
    11: [['collision', 'r1']],
}
eventsEnv = {
}