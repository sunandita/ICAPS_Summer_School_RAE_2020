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

rv.LOCATIONS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [3, 5, 7, 2, 4, 6], 1: [7], 2: [0, 5, 7, 3, 200], 3: [2, 5, 8, 200, 0, 7], 4: [0, 5], 5: [4, 0, 2, 3, 8, 200], 6: [0], 7: [2, 3, 0, 1], 8: [5, 3], 200: [2, 5, 3]}
rv.GROUND_WEIGHTS = {(0, 3): 5.468572385769171, (0, 5): 10.247611606410477, (0, 7): 9.486712001346874, (0, 2): 9.393199283608991, (0, 4): 1, (0, 6): 11.649077709924217, (1, 7): 12.183899539436961, (2, 5): 7.831776663465333, (2, 7): 7.706914598253908, (2, 3): 2.603281439027885, (2, 200): 5.784848499322798, (3, 5): 12.413083624331835, (3, 8): 10.356563246474627, (3, 200): 15.193997482453465, (3, 7): 9.813427914408999, (4, 5): 5.615408781632485, (5, 8): 9.055457803063087, (5, 200): 3.0095877993792977}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1,  'r4': rv.FACTORY1,  'r5': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.5172122917890025, 'r1': 6.008349094440421, 'r2': 7.148082740596063, 'r3': 5.5975379491857105, 'r4': 6.782998213275495, 'r5': 9.31834185598753}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 5.779212101918089, 'o1': 9.31834185598753, 'o2': 7.058254693762422}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2']}

    state.loc = { 'r0': 5, 'r1': 2, 'r2': 200, 'r3': 7, 'r4': 5, 'r5': 5, 'm0': 0, 'm1': 5, 'm2': 7, 'p0': 4, 'p1': 3, 'o0': 4, 'o1': 200, 'o2': 7,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL, 'r5': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'r4': False, 'r5': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 8, 'm1': 9, 'm2': 17}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    5: [['orderStart', ['type0']]],
    2: [['orderStart', ['type0']]],
}
eventsEnv = {
}