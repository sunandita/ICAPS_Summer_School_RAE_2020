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
rv.SHIPPING_DOC = {rv.FACTORY1: 5}

rv.GROUND_EDGES = {0: [4, 1, 3, 6], 1: [0, 2, 6, 4], 2: [3, 4, 1], 3: [0, 5, 2, 200], 4: [1, 0, 2, 5, 6, 200], 5: [3, 4, 200], 6: [0, 1, 4, 200], 200: [3, 4, 5, 6]}
rv.GROUND_WEIGHTS = {(0, 4): 3.7114045836700926, (0, 1): 16.582256041080953, (0, 3): 4.360728449589024, (0, 6): 9.191903886215481, (1, 2): 10.316006864261542, (1, 6): 3.63443489989516, (1, 4): 7.877471762129452, (2, 3): 6.1285805048693005, (2, 4): 2.802622828853572, (3, 5): 9.892761065015534, (3, 200): 8.652424394593528, (4, 5): 9.410306956814729, (4, 6): 16.171547786734067, (4, 200): 4.051490367489939, (5, 200): 6.207596253642537, (6, 200): 11.44609826121528}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 9.156544533379272, 'r1': 6.1959978510978875}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 7.6645658938254515, 'o1': 6.320232976867616, 'o2': 7.34601585350011, 'o3': 3.4157695568101567}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 6, 'r1': 2, 'm0': 4, 'p0': 4, 'p1': 0, 'p2': 200, 'o0': 0, 'o1': 2, 'o2': 5, 'o3': 2,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 4}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    6: [['orderStart', ['type0']]],
    3: [['orderStart', ['type0']]],
}
eventsEnv = {
}