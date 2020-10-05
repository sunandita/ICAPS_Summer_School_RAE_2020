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
rv.SHIPPING_DOC = {rv.FACTORY1: 4}

rv.GROUND_EDGES = {0: [4, 5, 6, 2, 200], 1: [4, 2, 3, 6], 2: [0, 1, 6, 4, 200], 3: [1, 6, 5, 200], 4: [2, 200, 0, 1], 5: [3, 6, 0], 6: [0, 1, 3, 2, 5], 200: [0, 2, 3, 4]}
rv.GROUND_WEIGHTS = {(0, 4): 9.337487829700931, (0, 5): 7.208518501022403, (0, 6): 6.993606811827891, (0, 2): 3.974397048908009, (0, 200): 10.892266857831023, (1, 4): 12.3142751173874, (1, 2): 2.413731015756225, (1, 3): 16.285113530727457, (1, 6): 6.3385025908667325, (2, 6): 9.418817198829359, (2, 4): 8.117297421397534, (2, 200): 8.306744303284647, (3, 6): 7.271172470631052, (3, 5): 8.436602817707472, (3, 200): 6.4021916172353786, (4, 200): 10.803995533934783, (5, 6): 7.129970387936154}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.665896338624101}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 6.665896338624101, 'o1': 6.665896338624101, 'o2': 4.923760716114105, 'o3': 4.2616080809241845, 'o4': 6.665896338624101}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2', 'o3', 'o4']}

    state.loc = { 'r0': 2, 'm0': 200, 'p0': 2, 'p1': 5, 'p2': 200, 'o0': 200, 'o1': 1, 'o2': 5, 'o3': 1, 'o4': 200,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 12}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    5: [['orderStart', ['type0']]],
    6: [['orderStart', ['type1']]],
}
eventsEnv = {
}