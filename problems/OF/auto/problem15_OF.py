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

rv.LOCATIONS = [0, 1, 2, 3, 4, 5, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 5, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 4}

rv.GROUND_EDGES = {0: [3, 4, 2], 1: [2, 3, 200], 2: [0, 1, 3, 5, 200], 3: [0, 1, 2, 4], 4: [3, 200, 0, 5], 5: [2, 4], 200: [1, 2, 4]}
rv.GROUND_WEIGHTS = {(0, 3): 8.779105388245192, (0, 4): 6.454792263855355, (0, 2): 2.857218044921681, (1, 2): 8.38932373857443, (1, 3): 10.084912726492831, (1, 200): 7.96413167712405, (2, 3): 5.841601946929807, (2, 5): 4.973979695752783, (2, 200): 1, (3, 4): 2.339638006550307, (4, 200): 11.516889218004795, (4, 5): 7.068676254962782}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.970482108851515, 'r1': 8.498725961822334, 'r2': 6.624355782618307, 'r3': 7.9238442294926505}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 7.159119690666393, 'o1': 8.172339775969895, 'o2': 6.19695659178162, 'o3': 6.431072797043446, 'o4': 6.297478840452853}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2', 'o3', 'o4']}

    state.loc = { 'r0': 1, 'r1': 5, 'r2': 200, 'r3': 5, 'm0': 5, 'p0': 3, 'o0': 5, 'o1': 200, 'o2': 2, 'o3': 4, 'o4': 4,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False}
    state.numUses = {'m0': 7}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    4: [['orderStart', ['type0']]],
    2: [['orderStart', ['type1']]],
}
eventsEnv = {
}