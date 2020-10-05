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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 2, 200, 4, 5], 1: [0, 6], 2: [3, 4, 5, 0], 3: [4, 2, 5], 4: [0, 3, 2], 5: [0, 3, 2, 6], 6: [1, 5, 200], 200: [6, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 10.699122325616736, (0, 2): 3.255127913426752, (0, 200): 13.039106588975798, (0, 4): 11.481833426824705, (0, 5): 5.2159040803071814, (1, 6): 2.313376453676118, (2, 3): 5.077534824652499, (2, 4): 9.588366765890344, (2, 5): 10.772429071641824, (3, 4): 5.532338046459553, (3, 5): 9.094945993060804, (5, 6): 9.957166433189423, (6, 200): 4.8821313472606604}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.706231965930474}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 5.075060054192034, 'o1': 4.827558450887605, 'o2': 6.706231965930474, 'o3': 6.706231965930474}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2', 'o3']}

    state.loc = { 'r0': 0, 'm0': 200, 'p0': 200, 'o0': 1, 'o1': 200, 'o2': 4, 'o3': 3,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 10}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    6: [['orderStart', ['type0']]],
    3: [['orderStart', ['type1']]],
}
eventsEnv = {
}