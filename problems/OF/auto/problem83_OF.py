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

rv.GROUND_EDGES = {0: [1, 200, 2, 3], 1: [2, 3, 0, 4], 2: [0, 4, 1, 200], 3: [0, 1, 200], 4: [1, 2, 200], 200: [0, 2, 3, 4]}
rv.GROUND_WEIGHTS = {(0, 1): 7.686682141979873, (0, 200): 11.390207762673896, (0, 2): 11.16619469494721, (0, 3): 9.535269413263926, (1, 2): 11.315674348762872, (1, 3): 6.448358326711464, (1, 4): 13.65351941944812, (2, 4): 2.719318473016492, (2, 200): 7.613881599915186, (3, 200): 6.050775919959388, (4, 200): 8.579401543898712}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.09658040213706, 'r1': 7.499080496339163, 'r2': 4.871818889935722, 'r3': 10.52931019337448}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True,  'o7': True,  'o8': True, }
    state.OBJ_WEIGHT = {'o0': 10.52931019337448, 'o1': 6.72545321028108, 'o2': 6.379469455707134, 'o3': 8.498795097282391, 'o4': 9.457389892835517, 'o5': 4.539719560431067, 'o6': 7.406019332961563, 'o7': 6.411892711241235, 'o8': 5.9751535158118365}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2', 'o3'], 'type2': ['o4', 'o5', 'o6', 'o7', 'o8']}

    state.loc = { 'r0': 4, 'r1': 4, 'r2': 3, 'r3': 1, 'm0': 0, 'm1': 200, 'p0': 4, 'p1': 2, 'p2': 2, 'o0': 1, 'o1': 0, 'o2': 0, 'o3': 2, 'o4': 2, 'o5': 0, 'o6': 3, 'o7': 3, 'o8': 2,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 11, 'm1': 7}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}