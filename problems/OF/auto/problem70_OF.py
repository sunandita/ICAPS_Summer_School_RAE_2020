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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [2, 3, 200, 1], 1: [0], 2: [3, 0, 4, 200], 3: [4, 0, 2], 4: [2, 3], 200: [0, 2]}
rv.GROUND_WEIGHTS = {(0, 2): 11.358716325346052, (0, 3): 8.651284643894625, (0, 200): 12.918758655310889, (0, 1): 7.539672683826507, (2, 3): 7.266273880444587, (2, 4): 9.32993830111395, (2, 200): 3.2038663084011416, (3, 4): 7.799013479006909}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1,  'r4': rv.FACTORY1,  'r5': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.988813480466467, 'r1': 7.780203230773683, 'r2': 8.463190879102802, 'r3': 9.063848110368474, 'r4': 9.330482629797515, 'r5': 9.232457002085837}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True, }
    state.OBJ_WEIGHT = {'o0': 7.570077184592684, 'o1': 6.312538899694487, 'o2': 4.6296533803865305, 'o3': 6.617344580275818, 'o4': 5.795601704702676, 'o5': 4.001289408678174}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3'], 'type1': ['o4'], 'type2': ['o5']}

    state.loc = { 'r0': 0, 'r1': 200, 'r2': 1, 'r3': 1, 'r4': 4, 'r5': 200, 'm0': 1, 'm1': 0, 'm2': 3, 'm3': 4, 'p0': 2, 'p1': 4, 'p2': 2, 'o0': 3, 'o1': 3, 'o2': 0, 'o3': 0, 'o4': 0, 'o5': 3,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL, 'r5': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'r4': False, 'r5': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False}
    state.numUses = {'m0': 16, 'm1': 14, 'm2': 9, 'm3': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type1']]],
    3: [['orderStart', ['type2']]],
}
eventsEnv = {
}