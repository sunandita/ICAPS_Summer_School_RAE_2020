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

rv.GROUND_EDGES = {0: [1, 3, 200], 1: [2, 0, 4], 2: [1, 3], 3: [0, 200, 2, 4], 4: [1, 3], 200: [0, 3]}
rv.GROUND_WEIGHTS = {(0, 1): 4.669250099526321, (0, 3): 8.862889805017915, (0, 200): 1.1101703900157531, (1, 2): 7.149028742597653, (1, 4): 8.15566968020866, (2, 3): 8.047470145826273, (3, 200): 4.223586680588564, (3, 4): 13.052640386818043}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.7030839253563395}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True, }
    state.OBJ_WEIGHT = {'o0': 7.7030839253563395, 'o1': 7.7030839253563395, 'o2': 5.877712196337419, 'o3': 7.7030839253563395, 'o4': 6.5698279077359825, 'o5': 7.7030839253563395, 'o6': 7.132127821799042}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3'], 'type1': ['o4', 'o5', 'o6']}

    state.loc = { 'r0': 0, 'm0': 0, 'p0': 200, 'o0': 2, 'o1': 4, 'o2': 4, 'o3': 200, 'o4': 2, 'o5': 0, 'o6': 1,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 14}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    7: [['orderStart', ['type0']]],
}
eventsEnv = {
}