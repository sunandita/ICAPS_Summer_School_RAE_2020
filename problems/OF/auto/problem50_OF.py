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
rv.SHIPPING_DOC = {rv.FACTORY1: 1}

rv.GROUND_EDGES = {0: [5, 6, 4], 1: [2, 5, 7, 200], 2: [3, 5, 1, 7], 3: [4, 2, 7, 200], 4: [0, 3, 5], 5: [2, 4, 0, 1, 6], 6: [5, 0], 7: [2, 3, 1], 200: [3, 1]}
rv.GROUND_WEIGHTS = {(0, 5): 1, (0, 6): 12.780347394811297, (0, 4): 14.039879205640858, (1, 2): 1.807361018701961, (1, 5): 8.574150446152094, (1, 7): 5.684730330679724, (1, 200): 13.519908916855425, (2, 3): 5.31665350867007, (2, 5): 10.779604670982208, (2, 7): 5.644816461746832, (3, 4): 5.940740605637421, (3, 7): 10.032826310246485, (3, 200): 15.88063090549323, (4, 5): 1, (5, 6): 8.363619665708075}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1,  'r4': rv.FACTORY1,  'r5': rv.FACTORY1,  'r6': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.174548780209071, 'r1': 7.888950393237086, 'r2': 8.94839227413827, 'r3': 6.109450732637805, 'r4': 9.243688988204152, 'r5': 7.653146729308341, 'r6': 7.00850756111181}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True, }
    state.OBJ_WEIGHT = {'o0': 7.480383025618398, 'o1': 6.5298717875512144, 'o2': 7.016331420516707, 'o3': 9.243688988204152, 'o4': 2.365805663120769, 'o5': 8.404532434838684}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3', 'o4', 'o5']}

    state.loc = { 'r0': 1, 'r1': 6, 'r2': 7, 'r3': 6, 'r4': 2, 'r5': 3, 'r6': 1, 'm0': 6, 'p0': 7, 'o0': 3, 'o1': 3, 'o2': 6, 'o3': 6, 'o4': 4, 'o5': 4,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL, 'r5': NIL, 'r6': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'r4': False, 'r5': False, 'r6': False, 'm0': False}
    state.numUses = {'m0': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}