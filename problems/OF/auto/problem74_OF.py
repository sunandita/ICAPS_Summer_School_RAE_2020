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
rv.SHIPPING_DOC = {rv.FACTORY1: 2}

rv.GROUND_EDGES = {0: [3, 1, 2, 5, 6, 200], 1: [0, 6], 2: [0, 200], 3: [0, 4, 200], 4: [5, 6, 3], 5: [0, 4], 6: [0, 1, 4], 200: [0, 3, 2]}
rv.GROUND_WEIGHTS = {(0, 3): 12.240983720916823, (0, 1): 12.03886605521486, (0, 2): 8.112155349250513, (0, 5): 10.291983462399575, (0, 6): 9.71420223895884, (0, 200): 5.207057019356913, (1, 6): 11.545782045106275, (2, 200): 1, (3, 4): 14.77540653402492, (3, 200): 8.45551222512597, (4, 5): 14.158386389372671, (4, 6): 4.842005936873658}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.302390730795354, 'r1': 7.304112394144697, 'r2': 10.58235246889589, 'r3': 10.324949218842853}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 8.159462793188876, 'o1': 8.162344694698227, 'o2': 8.059597740911125}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2']}

    state.loc = { 'r0': 3, 'r1': 200, 'r2': 2, 'r3': 2, 'm0': 3, 'm1': 200, 'm2': 4, 'm3': 1, 'p0': 3, 'p1': 5, 'o0': 200, 'o1': 1, 'o2': 4,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False}
    state.numUses = {'m0': 9, 'm1': 10, 'm2': 14, 'm3': 7}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}