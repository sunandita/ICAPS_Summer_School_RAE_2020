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
rv.SHIPPING_DOC = {rv.FACTORY1: 1}

rv.GROUND_EDGES = {0: [1, 3, 5, 200], 1: [0, 3, 200], 2: [5], 3: [0, 1], 4: [5, 200], 5: [0, 2, 4], 200: [0, 4, 1]}
rv.GROUND_WEIGHTS = {(0, 1): 11.187645254337719, (0, 3): 12.461006276809501, (0, 5): 8.53162121899128, (0, 200): 10.58773765307595, (1, 3): 14.912117917143785, (1, 200): 12.605156283335042, (2, 5): 9.459989464528226, (4, 5): 11.493982304323918, (4, 200): 6.940325624715621}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 9.552174679146221, 'r1': 9.540781161549077}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 8.884611550207051, 'o1': 6.244700264434977, 'o2': 5.809965999770643}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2']}

    state.loc = { 'r0': 3, 'r1': 5, 'm0': 0, 'p0': 0, 'o0': 2, 'o1': 1, 'o2': 200,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 7}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}