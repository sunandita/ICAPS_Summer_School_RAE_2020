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

rv.GROUND_EDGES = {0: [4, 5, 1, 6, 7], 1: [0, 200, 6], 2: [5], 3: [7, 4], 4: [0, 3, 5, 200], 5: [2, 0, 4, 6], 6: [0, 1, 5, 7], 7: [0, 3, 6, 200], 200: [4, 7, 1]}
rv.GROUND_WEIGHTS = {(0, 4): 12.709993674196575, (0, 5): 2.687301498474306, (0, 1): 9.856938861004961, (0, 6): 9.09600848692322, (0, 7): 8.933514911811404, (1, 200): 5.933378966647107, (1, 6): 7.1178894281036165, (2, 5): 3.3001025667766424, (3, 7): 6.138136581143388, (3, 4): 3.8334000959182166, (4, 5): 6.2356792411296755, (4, 200): 12.83325541533895, (5, 6): 1.2969042493296161, (6, 7): 5.29809160866758, (7, 200): 5.3643204260351505}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 5.6144253230441175, 'r1': 3.0672693717252866, 'r2': 6.435204912406581}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 5.569097698031902}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 5, 'r1': 7, 'r2': 3, 'm0': 6, 'm1': 200, 'p0': 6, 'o0': 200,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 7, 'm1': 8}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}