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

rv.LOCATIONS = [0, 1, 2, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [2, 200, 1], 1: [0, 2, 200], 2: [0, 1, 200], 200: [0, 1, 2]}
rv.GROUND_WEIGHTS = {(0, 2): 7.554080802628391, (0, 200): 8.733693056125984, (0, 1): 11.410367094339911, (1, 2): 6.888509114990249, (1, 200): 7.173489016684274, (2, 200): 6.377886844644856}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 9.198583703950508, 'r1': 9.36125135147031}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 5.741804174440668, 'o1': 8.102239191760043, 'o2': 9.36125135147031, 'o3': 4.987157923850116, 'o4': 9.36125135147031}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3'], 'type1': ['o4']}

    state.loc = { 'r0': 0, 'r1': 1, 'm0': 1, 'p0': 2, 'p1': 200, 'p2': 200, 'o0': 0, 'o1': 2, 'o2': 200, 'o3': 200, 'o4': 0,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 16}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    5: [['orderStart', ['type0']]],
}
eventsEnv = {
}