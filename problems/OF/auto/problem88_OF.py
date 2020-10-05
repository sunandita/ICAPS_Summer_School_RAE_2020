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

rv.GROUND_EDGES = {0: [2, 1, 3, 4, 6], 1: [0, 2, 5], 2: [1, 5, 0], 3: [0], 4: [0, 5, 200], 5: [1, 2, 4, 200], 6: [0, 200], 200: [4, 6, 5]}
rv.GROUND_WEIGHTS = {(0, 2): 8.521680579561588, (0, 1): 10.426654780340751, (0, 3): 6.573194204348102, (0, 4): 6.329202183901219, (0, 6): 12.00267292008596, (1, 2): 1.051846129612187, (1, 5): 6.546195164798178, (2, 5): 6.599304460626517, (4, 5): 7.327962803716306, (4, 200): 2.2099445280189656, (5, 200): 1.9050479433360872, (6, 200): 11.038238135896231}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.067041168993363, 'r1': 4.798122246822158}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True, }
    state.OBJ_WEIGHT = {'o0': 3.6040835201018098, 'o1': 7.244696740192646, 'o2': 8.067041168993363, 'o3': 8.067041168993363, 'o4': 3.4056428939709433, 'o5': 7.788996266343977}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3', 'o4', 'o5']}

    state.loc = { 'r0': 4, 'r1': 3, 'm0': 3, 'm1': 200, 'p0': 5, 'o0': 0, 'o1': 4, 'o2': 2, 'o3': 3, 'o4': 0, 'o5': 5,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 15, 'm1': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    4: [['orderStart', ['type0']]],
}
eventsEnv = {
}