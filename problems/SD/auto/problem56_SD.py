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
rv.EDGES = {1: [2, 3], 2: [1, 5, 6], 3: [1, 4], 4: [3], 5: [2, 7], 6: [2, 7], 7: [6, 5]}
rv.DOORLOCATIONS = {(6, 7): 'd1', (1, 2): 'd2'}
rv.ROBOTS = ['r1', 'r2', 'r3']
rv.DOORS = ['d1', 'd2']
rv.DOORTYPES = {'d1': 'ordinary', 'd2': 'spring'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed'}
    state.loc = {'r1': 3, 'r2': 2, 'r3': 7}
    state.pos = {'o1': 3, 'o2': 1, 'o3': 4}
    state.done = {0: False}
    state.doorType = {'d1': UNK, 'd2': UNK}

tasks = {
    5: [['moveTo', 'r3', 4]],
    5: [['moveTo', 'r3', 2]],
    5: [['moveTo', 'r1', 5]]
}

eventsEnv = {}

