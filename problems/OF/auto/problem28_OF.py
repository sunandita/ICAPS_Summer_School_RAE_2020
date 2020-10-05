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

rv.GROUND_EDGES = {0: [2, 3, 1, 4, 5], 1: [0, 200, 6], 2: [4, 0], 3: [4, 0, 6], 4: [0, 2, 3], 5: [0, 6], 6: [1, 3, 5, 200], 200: [6, 1]}
rv.GROUND_WEIGHTS = {(0, 2): 9.137164000158927, (0, 3): 10.259637800988362, (0, 1): 5.61177726378582, (0, 4): 5.283839421353532, (0, 5): 9.260591564672653, (1, 200): 4.965875391691461, (1, 6): 4.880326702902207, (2, 4): 7.3547121702360165, (3, 4): 12.439359485574947, (3, 6): 7.615940404419845, (5, 6): 4.459285348477471, (6, 200): 8.594572133450413}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.800731643413304, 'r1': 7.585633622763615, 'r2': 11.958267287735977, 'r3': 3.7734965338698734}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 6.043582498307149, 'o1': 6.297932902315507}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1']}

    state.loc = { 'r0': 0, 'r1': 6, 'r2': 0, 'r3': 5, 'm0': 1, 'm1': 1, 'p0': 200, 'o0': 4, 'o1': 4,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 9, 'm1': 6}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    2: [['orderStart', ['type0']]],
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}