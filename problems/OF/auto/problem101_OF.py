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

rv.GROUND_EDGES = {0: [5, 3, 4, 6], 1: [2, 5, 4], 2: [4, 5, 1, 200], 3: [0], 4: [0, 1, 2], 5: [0, 200, 1, 2], 6: [0], 200: [2, 5]}
rv.GROUND_WEIGHTS = {(0, 5): 5.022222239202312, (0, 3): 8.528369012542337, (0, 4): 10.033836162938506, (0, 6): 9.461343123205367, (1, 2): 7.419064328363229, (1, 5): 1, (1, 4): 14.145909164684525, (2, 4): 10.434708195129666, (2, 5): 8.70300866270794, (2, 200): 5.317768948954667, (5, 200): 7.603735602534347}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.4759630155807155, 'r1': 7.323284771317044, 'r2': 7.5315978644314105, 'r3': 9.147309704678513}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 6.1986585078056935, 'o1': 6.836739525337635, 'o2': 8.695243177592817}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2']}

    state.loc = { 'r0': 200, 'r1': 4, 'r2': 1, 'r3': 3, 'm0': 2, 'm1': 5, 'm2': 2, 'm3': 0, 'p0': 1, 'p1': 3, 'o0': 5, 'o1': 5, 'o2': 0,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False}
    state.numUses = {'m0': 12, 'm1': 10, 'm2': 8, 'm3': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    4: [['orderStart', ['type1']]],
}
eventsEnv = {
}