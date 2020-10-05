__author__ = 'mason'

from domain_orderFulfillment import *
from timer import DURATION
from state import state
import numpy as np

'''
This is a randomly generated problem
'''

def GetCostOfMove(id, r, loc1, loc2, dist):
    return 1 + dist

def GetCostOfLookup(id, item):
    return max(1, np.random.beta(2, 2))

def GetCostOfWrap(id, orderName, m, item):
    return max(1, np.random.normal(5, .5))

def GetCostOfPickup(id, r, item):
    return max(1, np.random.normal(4, 1))

def GetCostOfPutdown(id, r, item):
    return max(1, np.random.normal(4, 1))

def GetCostOfLoad(id, orderName, r, m, item):
    return max(1, np.random.normal(3, .5))

DURATION.TIME = {
    'lookupDB': GetCostOfLookup,
    'wrap': GetCostOfWrap,
    'pickup': GetCostOfPickup,
    'putdown': GetCostOfPutdown,
    'loadMachine': GetCostOfLoad,
    'moveRobot': GetCostOfMove,
    'acquireRobot': 1,
    'freeRobot': 1,
    'wait': 5
}

DURATION.COUNTER = {
    'lookupDB': GetCostOfLookup,
    'wrap': GetCostOfWrap,
    'pickup': GetCostOfPickup,
    'putdown': GetCostOfPutdown,
    'loadMachine': GetCostOfLoad,
    'moveRobot': GetCostOfMove,
    'acquireRobot': 1,
    'freeRobot': 1,
    'wait': 5
}

rv.LOCATIONS = [0, 1, 2, 3, 4, 5, 6, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 5, 6, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 4}

rv.GROUND_EDGES = {0: [4, 2, 3, 5, 6], 1: [5, 4], 2: [0, 5, 4], 3: [0], 4: [1, 2, 200, 0], 5: [0, 1, 2, 200], 6: [0, 200], 200: [5, 6, 4]}
rv.GROUND_WEIGHTS = {(0, 4): 12.51553891669746, (0, 2): 4.443960094335424, (0, 3): 7.274810576629561, (0, 5): 7.431680263544831, (0, 6): 7.720218462533336, (1, 5): 7.388396279708221, (1, 4): 11.13947971021927, (2, 5): 10.023219518023247, (2, 4): 9.893364798331161, (4, 200): 7.546309834279353, (5, 200): 9.488252970476614, (6, 200): 10.250550553564452}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 10.417911367813648, 'r1': 8.50159961780665}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 8.897358268962936}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 0, 'r1': 6, 'm0': 6, 'p0': 2, 'o0': 3,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 15}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}