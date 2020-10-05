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
rv.SHIPPING_DOC = {rv.FACTORY1: 5}

rv.GROUND_EDGES = {0: [3, 5, 200], 1: [2, 3, 6], 2: [5, 6, 1], 3: [0, 1, 4], 4: [3, 6], 5: [2, 200, 0, 6], 6: [1, 2, 4, 5], 200: [0, 5]}
rv.GROUND_WEIGHTS = {(0, 3): 12.773137382973939, (0, 5): 7.822566916962562, (0, 200): 1, (1, 2): 16.532085057009525, (1, 3): 3.433288078800431, (1, 6): 10.936637506391893, (2, 5): 10.094158133943136, (2, 6): 5.041206644265815, (3, 4): 9.833586782755441, (4, 6): 10.702602047318551, (5, 200): 6.015462754399343, (5, 6): 13.250237387032076}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.258459171816909, 'r1': 8.371619810564145}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True, }
    state.OBJ_WEIGHT = {'o0': 4.805536368813449, 'o1': 8.371619810564145, 'o2': 5.2766424240838905, 'o3': 6.076107003300658, 'o4': 8.371619810564145, 'o5': 7.312145113495467}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3', 'o4', 'o5']}

    state.loc = { 'r0': 200, 'r1': 0, 'm0': 200, 'p0': 0, 'o0': 200, 'o1': 200, 'o2': 200, 'o3': 200, 'o4': 0, 'o5': 3,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 13}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}