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

rv.LOCATIONS = [1, 2, 3, 4, 5, 6]
rv.EDGES = {1: [2, 3], 2: [1, 6], 3: [1, 4], 4: [3, 5], 5: [4], 6: [2]}
rv.DOORLOCATIONS = {(2, 6): 'd1', (4, 5): 'd2'}
rv.ROBOTS = ['r3', 'r2', 'r1']
rv.DOORS = ['d1', 'd2']
rv.DOORTYPES = {'d1': 'spring', 'd2': 'spring'}

def ResetState():
    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}
    state.doorStatus = {'d1': 'closed', 'd2': 'closed'}
    state.loc = {'r1': 2, 'r2': 3, 'r3': 2}
    state.pos = {'o1': 4, 'o2': 6, 'o3': 4}
    state.doorType = {'d1': UNK, 'd2': UNK}
    state.status = {'r1': 'free', 'r2': 'free', 'r3': 'free'}
tasks = {
    2: [['fetch', 'r3', 'o1', 5]],
    #4: [['fetch', 'r2', 'o3', 4]]
}

eventsEnv = {}

