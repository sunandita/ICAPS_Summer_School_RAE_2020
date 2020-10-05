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
rv.EDGES = {1: [2, 5], 2: [1, 3], 3: [2, 4], 4: [3, 6, 7], 5: [1, 7], 6: [4], 7: [4, 5]}
rv.DOORLOCATIONS = {(1, 5): 'd1', (5, 7): 'd2', (2, 3): 'd3', (3, 4): 'd4', (4, 7): 'd5', (4, 6): 'd6'}
rv.ROBOTS = ['r1', 'r2']
rv.DOORS = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6']
rv.DOORTYPES = {'d1': 'ordinary', 'd2': 'spring', 'd3': 'spring', 'd4': 'spring', 'd5': 'ordinary', 'd6': 'spring'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed', 'd4': 'closed', 'd5': 'closed', 'd6': 'closed'}
    state.loc = {'r1': 2, 'r2': 1}
    state.pos = {'o1': 7, 'o2': 5}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK, 'd4': UNK, 'd5': UNK, 'd6': UNK}

tasks = {
    5: [['moveTo', 'r1', 5]],
    3: [['moveTo', 'r1', 1]]
}

eventsEnv = {}

