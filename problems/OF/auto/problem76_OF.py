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
rv.SHIPPING_DOC = {rv.FACTORY1: 1}

rv.GROUND_EDGES = {0: [2, 4, 5, 6], 1: [6, 200, 4, 5], 2: [0, 4], 3: [5, 4, 6], 4: [1, 2, 3, 0], 5: [1, 0, 3], 6: [0, 3, 1, 200], 200: [6, 1]}
rv.GROUND_WEIGHTS = {(0, 2): 2.676808592111697, (0, 4): 10.863890589861274, (0, 5): 11.638255922290352, (0, 6): 12.5122633259062, (1, 6): 15.384401543391405, (1, 200): 10.9119557025878, (1, 4): 5.326658030177167, (1, 5): 9.422997308872118, (2, 4): 1, (3, 5): 12.583548995846659, (3, 4): 8.04259342548185, (3, 6): 13.35336810487601, (6, 200): 11.341147188012425}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.819346564745427}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 5.301541223307222, 'o1': 6.819346564745427}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1']}

    state.loc = { 'r0': 5, 'm0': 1, 'm1': 6, 'm2': 4, 'p0': 0, 'o0': 1, 'o1': 4,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 16, 'm1': 8, 'm2': 15}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    3: [['orderStart', ['type1']]],
}
eventsEnv = {
}