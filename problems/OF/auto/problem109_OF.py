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
rv.SHIPPING_DOC = {rv.FACTORY1: 5}

rv.GROUND_EDGES = {0: [4, 1, 2, 5], 1: [0, 6, 7], 2: [0, 3, 200], 3: [2, 5, 200], 4: [0], 5: [0, 3, 7, 200], 6: [1, 7], 7: [1, 6, 5], 200: [2, 3, 5]}
rv.GROUND_WEIGHTS = {(0, 4): 10.759338551673594, (0, 1): 7.113779828082287, (0, 2): 5.158994538400462, (0, 5): 6.230864831455877, (1, 6): 10.163099604096303, (1, 7): 10.62219775642977, (2, 3): 4.593062103797658, (2, 200): 10.873465965473805, (3, 5): 7.740879953860147, (3, 200): 3.6233210478624356, (5, 7): 10.029234312693413, (5, 200): 1.5659577553987596, (6, 7): 8.43043759845897}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.262247631957051}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1,  'm4': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 4.262247631957051}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 0, 'm0': 200, 'm1': 200, 'm2': 200, 'm3': 200, 'm4': 0, 'p0': 5, 'p1': 7, 'p2': 2, 'o0': 4,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False, 'm4': False}
    state.numUses = {'m0': 9, 'm1': 16, 'm2': 11, 'm3': 6, 'm4': 19}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}