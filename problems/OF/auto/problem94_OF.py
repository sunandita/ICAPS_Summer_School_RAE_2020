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

rv.GROUND_EDGES = {0: [6, 4, 5], 1: [6, 200, 7], 2: [5, 7, 3, 200], 3: [2], 4: [0, 6], 5: [0, 2], 6: [4, 0, 1], 7: [1, 2], 200: [2, 1]}
rv.GROUND_WEIGHTS = {(0, 6): 12.696586409361172, (0, 4): 7.884517678450143, (0, 5): 8.451055099522353, (1, 6): 8.620308885865441, (1, 200): 13.229297015870312, (1, 7): 3.0902489746001223, (2, 5): 7.592246039693506, (2, 7): 7.278461208962594, (2, 3): 3.1917316054057165, (2, 200): 8.21185992912687, (4, 6): 3.313809510468376}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.186253079013151, 'r1': 6.245404428706281}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 6.245404428706281, 'o1': 6.245404428706281, 'o2': 6.245404428706281, 'o3': 3.984094592639039}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2', 'o3']}

    state.loc = { 'r0': 1, 'r1': 200, 'm0': 7, 'p0': 3, 'o0': 5, 'o1': 1, 'o2': 2, 'o3': 4,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False}
    state.numUses = {'m0': 15}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    2: [['orderStart', ['type0']]],
    3: [['orderStart', ['type1']]],
}
eventsEnv = {
}