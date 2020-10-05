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
rv.EDGES = {1: [2, 4], 2: [1, 3, 7], 3: [2], 4: [1, 5], 5: [4, 6], 6: [5, 7], 7: [6, 2, 8], 8: [7]}
rv.DOORLOCATIONS = {(7, 8): 'd1', (6, 7): 'd2', (1, 4): 'd3', (2, 7): 'd4', (1, 2): 'd5', (5, 6): 'd6'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'ordinary', 'd3': 'ordinary', 'd4': 'spring', 'd5': 'spring', 'd6': 'ordinary'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed', 'd5': 'closed', 'd6': 'closed'}
    state.loc = {'r1': 1, 'r2': 4}
    state.pos = {'o1': 4, 'o2': 5}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK, 'd5': UNK, 'd6': UNK}

tasks = {
    4: [['moveTo', 'r2', 5]],
    2: [['moveTo', 'r2', 2]]
}

eventsEnv = {}

