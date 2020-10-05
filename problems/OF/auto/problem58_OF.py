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

rv.GROUND_EDGES = {0: [1, 4, 2, 6], 1: [0, 3], 2: [0, 200, 3, 4], 3: [1, 2, 5, 200], 4: [2, 0, 5, 200], 5: [3, 4, 6], 6: [0, 5], 200: [3, 4, 2]}
rv.GROUND_WEIGHTS = {(0, 1): 11.413368948898801, (0, 4): 4.489938264284073, (0, 2): 8.504128693881471, (0, 6): 4.820997450917684, (1, 3): 11.006722624812951, (2, 200): 4.763154278322576, (2, 3): 1.60290257323953, (2, 4): 6.423596750036273, (3, 5): 7.14028050489894, (3, 200): 10.411078204272641, (4, 5): 9.875251477556867, (4, 200): 14.673413054084314, (5, 6): 11.25392250643753}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 3.653924527341622, 'r1': 6.2415019573904305}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 6.2415019573904305}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 6, 'r1': 1, 'm0': 4, 'm1': 6, 'm2': 2, 'p0': 4, 'o0': 4,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 8, 'm1': 6, 'm2': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}