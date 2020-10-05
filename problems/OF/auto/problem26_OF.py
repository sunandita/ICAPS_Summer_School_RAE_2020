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

rv.GROUND_EDGES = {0: [1, 3, 5], 1: [0, 200, 2], 2: [1, 4, 3], 3: [2, 0, 4], 4: [3, 2], 5: [0], 200: [1]}
rv.GROUND_WEIGHTS = {(0, 1): 4.5218687845721295, (0, 3): 1, (0, 5): 9.636922015395795, (1, 200): 12.551343131231476, (1, 2): 6.266078385006994, (2, 4): 6.803865563934225, (2, 3): 13.988796689962669, (3, 4): 10.194338200005351}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.189325385642108, 'r1': 7.667377322107325, 'r2': 8.861803818235803}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1,  'm4': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 7.741901844537928, 'o1': 5.235100994410653}
    state.OBJ_CLASS = {'type0': ['o0', 'o1']}

    state.loc = { 'r0': 3, 'r1': 200, 'r2': 4, 'm0': 3, 'm1': 1, 'm2': 0, 'm3': 0, 'm4': 2, 'p0': 5, 'o0': 2, 'o1': 3,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False, 'm4': False}
    state.numUses = {'m0': 12, 'm1': 8, 'm2': 13, 'm3': 11, 'm4': 8}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}