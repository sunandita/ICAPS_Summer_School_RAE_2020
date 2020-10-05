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

rv.LOCATIONS = [0, 1, 2, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 200], 1: [0, 2, 200], 2: [1, 200], 200: [0, 1, 2]}
rv.GROUND_WEIGHTS = {(0, 1): 11.768799310803852, (0, 200): 2.0893129762919607, (1, 2): 5.126256219011529, (1, 200): 8.867911083139626, (2, 200): 12.12931446103809}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.50263556976414, 'r1': 6.261630278701368, 'r2': 7.857138747440315}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 7.857138747440315, 'o1': 7.857138747440315, 'o2': 2.6724249591505957, 'o3': 5.096348044671836}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 1, 'r1': 200, 'r2': 1, 'm0': 200, 'm1': 0, 'm2': 200, 'p0': 0, 'o0': 2, 'o1': 2, 'o2': 1, 'o3': 2,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 6, 'm1': 7, 'm2': 10}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    2: [['orderStart', ['type0']]],
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}