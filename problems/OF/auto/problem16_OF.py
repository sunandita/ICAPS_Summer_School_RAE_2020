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

rv.LOCATIONS = [0, 1, 2, 3, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [2, 200, 3], 1: [2, 200], 2: [0, 1, 3, 200], 3: [0, 2], 200: [1, 2, 0]}
rv.GROUND_WEIGHTS = {(0, 2): 8.683926212572246, (0, 200): 6.530047901809786, (0, 3): 3.544856651062462, (1, 2): 6.924259844583896, (1, 200): 9.946525135501295, (2, 3): 10.180045821456584, (2, 200): 13.022197221001363}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 10.004719818230367}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True, }
    state.OBJ_WEIGHT = {'o0': 9.748639002995153, 'o1': 4.664374047843726, 'o2': 6.859262374639023, 'o3': 7.081806348690943, 'o4': 7.581908487412777, 'o5': 10.004719818230367, 'o6': 6.584313945127038}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3'], 'type1': ['o4', 'o5', 'o6']}

    state.loc = { 'r0': 2, 'm0': 1, 'p0': 2, 'o0': 3, 'o1': 200, 'o2': 0, 'o3': 3, 'o4': 3, 'o5': 200, 'o6': 0,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    5: [['orderStart', ['type0']]],
    2: [['orderStart', ['type0']]],
}
eventsEnv = {
}