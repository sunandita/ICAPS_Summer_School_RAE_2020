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
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [1, 2, 3, 200], 1: [0, 3, 2], 2: [1, 3, 4, 0], 3: [0, 1, 4, 200, 2], 4: [2, 3], 200: [0, 3]}
rv.GROUND_WEIGHTS = {(0, 1): 11.828468769315458, (0, 2): 4.7991266647615465, (0, 3): 6.411342092646026, (0, 200): 9.437318796217115, (1, 3): 8.052240789916658, (1, 2): 5.708765106132287, (2, 3): 6.191781936688989, (2, 4): 6.650296510717869, (3, 4): 10.359642796443733, (3, 200): 3.8782820436032637}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.034922006166774, 'r1': 7.912664799293761, 'r2': 9.98502112279469, 'r3': 10.551447990504895}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1,  'm4': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 7.817714516771931}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 2, 'r1': 2, 'r2': 3, 'r3': 200, 'm0': 1, 'm1': 0, 'm2': 200, 'm3': 4, 'm4': 3, 'p0': 3, 'p1': 1, 'o0': 1,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False, 'm4': False}
    state.numUses = {'m0': 10, 'm1': 13, 'm2': 7, 'm3': 10, 'm4': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}