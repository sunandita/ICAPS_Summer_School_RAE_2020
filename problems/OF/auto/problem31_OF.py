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

rv.LOCATIONS = [0, 1, 2, 3, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 200], 1: [0, 2, 3, 200], 2: [1, 3, 200], 3: [1, 2], 200: [0, 1, 2]}
rv.GROUND_WEIGHTS = {(0, 1): 12.60763448992882, (0, 200): 9.89863572980953, (1, 2): 8.346711200228176, (1, 3): 7.069838519742104, (1, 200): 4.70693278171893, (2, 3): 10.526279141411713, (2, 200): 9.54241377793227}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.4116857535645275}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 7.4116857535645275, 'o1': 7.4116857535645275, 'o2': 3.944413000881914, 'o3': 7.4116857535645275, 'o4': 6.694104791621712}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2', 'o3', 'o4']}

    state.loc = { 'r0': 200, 'm0': 0, 'p0': 3, 'p1': 0, 'o0': 3, 'o1': 1, 'o2': 2, 'o3': 200, 'o4': 0,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 7}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}