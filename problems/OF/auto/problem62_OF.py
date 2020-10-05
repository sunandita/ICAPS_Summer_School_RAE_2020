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

rv.GROUND_EDGES = {0: [1, 2, 4, 200, 3], 1: [2, 4, 0, 3, 200], 2: [4, 0, 1], 3: [0, 1, 4], 4: [3, 0, 1, 2], 200: [1, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 8.339734977426263, (0, 2): 12.782471204845653, (0, 4): 1.4573925753056773, (0, 200): 1.9054250683218728, (0, 3): 4.193557905999012, (1, 2): 15.777006308874313, (1, 4): 10.742111749991842, (1, 3): 7.534473584229431, (1, 200): 6.632985362706415, (2, 4): 5.1167109230895, (3, 4): 1.2180650914526048}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.642981441266107}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True,  'o7': True,  'o8': True, }
    state.OBJ_WEIGHT = {'o0': 4.642981441266107, 'o1': 4.642981441266107, 'o2': 4.642981441266107, 'o3': 3.978811029733769, 'o4': 4.642981441266107, 'o5': 4.642981441266107, 'o6': 4.642981441266107, 'o7': 3.9377798836061166, 'o8': 4.642981441266107}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2', 'o3', 'o4'], 'type2': ['o5'], 'type3': ['o6', 'o7', 'o8']}

    state.loc = { 'r0': 0, 'm0': 4, 'm1': 1, 'm2': 200, 'p0': 2, 'o0': 4, 'o1': 3, 'o2': 1, 'o3': 200, 'o4': 3, 'o5': 0, 'o6': 2, 'o7': 2, 'o8': 3,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 4, 'm1': 9, 'm2': 13}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    15: [['orderStart', ['type0']]],
    12: [['orderStart', ['type0']]],
}
eventsEnv = {
}