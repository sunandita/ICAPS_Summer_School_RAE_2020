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

rv.LOCATIONS = [0, 1, 2, 3, 4, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [3, 200, 1], 1: [0, 3], 2: [3, 4], 3: [1, 2, 0, 200], 4: [2], 200: [3, 0]}
rv.GROUND_WEIGHTS = {(0, 3): 1, (0, 200): 1, (0, 1): 9.185935020404624, (1, 3): 12.230158645963602, (2, 3): 6.723715180726013, (2, 4): 3.8948762191494026, (3, 200): 5.4264819026988755}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 5.9095680902752585}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 5.9095680902752585, 'o1': 5.387695384409574}
    state.OBJ_CLASS = {'type0': ['o0', 'o1']}

    state.loc = { 'r0': 0, 'm0': 4, 'm1': 0, 'm2': 2, 'p0': 200, 'o0': 0, 'o1': 3,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 11, 'm1': 11, 'm2': 7}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    2: [['orderStart', ['type0']]],
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}