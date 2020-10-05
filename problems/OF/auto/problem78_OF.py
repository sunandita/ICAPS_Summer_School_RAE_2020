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
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [1, 2, 5, 3, 200], 1: [0], 2: [0, 3, 5], 3: [0, 2, 5, 200], 4: [5], 5: [2, 0, 3, 4], 200: [0, 3]}
rv.GROUND_WEIGHTS = {(0, 1): 9.71505949832175, (0, 2): 13.657313643532735, (0, 5): 4.299817968067044, (0, 3): 8.11762996530363, (0, 200): 5.806769251085994, (2, 3): 8.413137172016226, (2, 5): 8.627776193402223, (3, 5): 2.5106830700863725, (3, 200): 8.73702048031201, (4, 5): 5.9306428351070615}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 10.408122641161102, 'r1': 9.725605049169175}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 4.4692965252004715, 'o1': 6.986465010600147, 'o2': 5.440976321491995, 'o3': 4.680581813988839}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 5, 'r1': 3, 'm0': 5, 'p0': 4, 'o0': 2, 'o1': 2, 'o2': 0, 'o3': 2,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    2: [['orderStart', ['type0']]],
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}