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

rv.LOCATIONS = [0, 1, 2, 3, 4, 5, 6, 7, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [7, 200, 2, 4, 5], 1: [2, 3, 7], 2: [0, 5, 1, 6], 3: [1, 7, 6, 200], 4: [0, 7], 5: [0, 2], 6: [2, 3, 200], 7: [1, 4, 0, 3, 200], 200: [3, 6, 7, 0]}
rv.GROUND_WEIGHTS = {(0, 7): 10.815053485930392, (0, 200): 6.720165992862466, (0, 2): 12.272790152907362, (0, 4): 13.91736716070272, (0, 5): 6.835362806643524, (1, 2): 7.19713125630838, (1, 3): 15.106482082702406, (1, 7): 8.733175648022963, (2, 5): 12.606173355785113, (2, 6): 10.551966889979187, (3, 7): 3.432580720127487, (3, 6): 10.861121589207006, (3, 200): 12.714335293812335, (4, 7): 11.9522162832432, (6, 200): 6.675531975257365, (7, 200): 4.025241763623583}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.122781379683412}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 6.798044008802611}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 4, 'm0': 4, 'p0': 3, 'o0': 4,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}