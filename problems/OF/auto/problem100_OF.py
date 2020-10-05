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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [5, 200, 4, 6], 1: [5, 2, 3], 2: [1, 5, 200], 3: [1, 4, 5], 4: [0, 3, 5, 200], 5: [2, 3, 6, 0, 1, 4], 6: [0, 5], 200: [2, 4, 0]}
rv.GROUND_WEIGHTS = {(0, 5): 1, (0, 200): 11.736455274240335, (0, 4): 6.768658545533844, (0, 6): 8.02085200477692, (1, 5): 5.486414008053737, (1, 2): 6.89192515220757, (1, 3): 7.300426741678524, (2, 5): 6.246771259584574, (2, 200): 7.553573711288545, (3, 4): 12.550288316936552, (3, 5): 7.2228382366994355, (4, 5): 8.281287658973715, (4, 200): 8.0895882523243, (5, 6): 8.324862737970296}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1,  'r4': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.20986131639863, 'r1': 9.205746451120117, 'r2': 10.084377516386981, 'r3': 7.852320918582579, 'r4': 7.51177619437544}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 6.9934178298240735, 'o1': 7.727869691609008, 'o2': 9.437170329293028, 'o3': 7.599918161876155}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 2, 'r1': 0, 'r2': 4, 'r3': 1, 'r4': 0, 'm0': 5, 'p0': 4, 'p1': 5, 'p2': 1, 'o0': 2, 'o1': 3, 'o2': 1, 'o3': 6,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'r4': False, 'm0': False}
    state.numUses = {'m0': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}