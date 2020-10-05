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
rv.EDGES = {1: [2], 2: [1, 3], 3: [2, 4, 6, 7], 4: [3, 5, 8], 5: [4], 6: [3], 7: [3], 8: [4]}
rv.DOORLOCATIONS = {(3, 6): 'd1', (4, 5): 'd2', (3, 7): 'd3', (2, 3): 'd4', (1, 2): 'd5', (3, 4): 'd6', (4, 8): 'd7'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'ordinary', 'd3': 'spring', 'd4': 'spring', 'd5': 'ordinary', 'd6': 'spring', 'd7': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed', 'd5': 'closed', 'd6': 'closed', 'd7': 'closed'}
    state.loc = {'r1': 6, 'r2': 2}
    state.pos = {'o1': 8, 'o2': 2}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK, 'd5': UNK, 'd6': UNK, 'd7': UNK}

tasks = {
    1: [['moveTo', 'r1', 4]],
    4: [['moveTo', 'r2', 3]]
}

eventsEnv = {}

