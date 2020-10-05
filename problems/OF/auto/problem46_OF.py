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

rv.GROUND_EDGES = {0: [2, 5, 200], 1: [2, 4], 2: [0, 3, 200, 1, 5], 3: [2, 5, 6, 4], 4: [3, 1], 5: [0, 2, 3], 6: [3, 200], 200: [0, 6, 2]}
rv.GROUND_WEIGHTS = {(0, 2): 8.027044976972928, (0, 5): 7.664332277944656, (0, 200): 1, (1, 2): 10.615295217716778, (1, 4): 1, (2, 3): 3.8513411013299743, (2, 200): 3.919258339127647, (2, 5): 11.014631078831863, (3, 5): 4.013269320892771, (3, 6): 6.427561303251464, (3, 4): 3.7369702407691383, (6, 200): 7.982535250666912}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.090114353922937}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 6.090114353922937, 'o1': 6.090114353922937, 'o2': 6.074868917825751, 'o3': 2.950944787369357}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 200, 'm0': 1, 'p0': 0, 'o0': 2, 'o1': 6, 'o2': 6, 'o3': 5,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 6}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}