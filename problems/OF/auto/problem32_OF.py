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
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [6, 1, 4], 1: [0, 6], 2: [6, 3, 5], 3: [2, 4, 200], 4: [0, 3], 5: [2, 200], 6: [0, 1, 2, 200], 200: [5, 6, 3]}
rv.GROUND_WEIGHTS = {(0, 6): 8.777747131871138, (0, 1): 3.513262951572507, (0, 4): 10.094329255407988, (1, 6): 6.655072078623958, (2, 6): 9.713395867034421, (2, 3): 7.028127259591442, (2, 5): 6.511053300922441, (3, 4): 10.63708702386415, (3, 200): 4.952901913718231, (5, 200): 2.1315538240914034, (6, 200): 10.049427072011737}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 9.060867958779987, 'r1': 7.599531440271114, 'r2': 6.814341321893631, 'r3': 10.008803151455462}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 4.561185700665841, 'o1': 8.790073210032755}
    state.OBJ_CLASS = {'type0': ['o0', 'o1']}

    state.loc = { 'r0': 3, 'r1': 5, 'r2': 0, 'r3': 4, 'm0': 4, 'p0': 3, 'o0': 5, 'o1': 6,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False}
    state.numUses = {'m0': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    2: [['orderStart', ['type0']]],
}
eventsEnv = {
}