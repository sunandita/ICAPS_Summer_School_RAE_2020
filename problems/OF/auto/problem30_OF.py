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
rv.SHIPPING_DOC = {rv.FACTORY1: 6}

rv.GROUND_EDGES = {0: [3, 5, 1, 2], 1: [0, 2, 5, 6], 2: [0, 1, 4, 7], 3: [0, 4, 6, 7], 4: [2, 3, 5, 7], 5: [1, 4, 6, 7, 0], 6: [1, 3, 7, 200, 5], 7: [2, 3, 4, 5, 6], 200: [6]}
rv.GROUND_WEIGHTS = {(0, 3): 10.217934539665697, (0, 5): 1.9577604025028403, (0, 1): 10.970309407674966, (0, 2): 7.831681723417763, (1, 2): 16.33388089989071, (1, 5): 9.209182303815558, (1, 6): 8.63557821314461, (2, 4): 12.658840988058337, (2, 7): 8.117084488766837, (3, 4): 11.471941764698368, (3, 6): 11.917619832409345, (3, 7): 10.702241109440042, (4, 5): 11.688038977265876, (4, 7): 12.54267933076871, (5, 6): 5.353962308712179, (5, 7): 2.270727422400573, (6, 7): 13.704876401932626, (6, 200): 1}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.018823064130384}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True, }
    state.OBJ_WEIGHT = {'o0': 6.366625487462509, 'o1': 7.998092441908041, 'o2': 8.018823064130384, 'o3': 8.018823064130384, 'o4': 7.001177401724661, 'o5': 8.018823064130384, 'o6': 6.303542325404729}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2'], 'type1': ['o3', 'o4', 'o5', 'o6']}

    state.loc = { 'r0': 5, 'm0': 4, 'm1': 2, 'p0': 0, 'o0': 6, 'o1': 3, 'o2': 3, 'o3': 2, 'o4': 4, 'o5': 3, 'o6': 3,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 7, 'm1': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    11: [['orderStart', ['type0']]],
}
eventsEnv = {
}