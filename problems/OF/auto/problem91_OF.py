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
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [1, 2, 3, 4, 200], 1: [4, 0], 2: [0, 4], 3: [0, 4, 200], 4: [0, 1, 2, 3], 200: [0, 3]}
rv.GROUND_WEIGHTS = {(0, 1): 9.29216263854809, (0, 2): 6.206776312450933, (0, 3): 6.599416609049529, (0, 4): 7.8553364363028555, (0, 200): 5.866312145482132, (1, 4): 10.086688273116037, (2, 4): 5.818295947263703, (3, 4): 9.120648267165912, (3, 200): 10.861633290022523}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.1590216367092765}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 5.514667090130479, 'o1': 3.395757730422439, 'o2': 4.476272143334308}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2']}

    state.loc = { 'r0': 0, 'm0': 2, 'p0': 200, 'o0': 1, 'o1': 3, 'o2': 1,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 4}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    2: [['orderStart', ['type0']]],
}
eventsEnv = {
}