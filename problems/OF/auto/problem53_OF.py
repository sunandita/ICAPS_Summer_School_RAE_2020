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
rv.SHIPPING_DOC = {rv.FACTORY1: 6}

rv.GROUND_EDGES = {0: [4, 6, 1], 1: [0, 2, 200], 2: [1, 8, 3, 7, 200], 3: [2, 4, 5, 8], 4: [7, 8, 0, 3, 5], 5: [4, 3, 200], 6: [0, 200, 7], 7: [2, 4, 6], 8: [3, 2, 4], 200: [1, 2, 5, 6]}
rv.GROUND_WEIGHTS = {(0, 4): 10.055195086027743, (0, 6): 3.6691123433636488, (0, 1): 1.0849030342693409, (1, 2): 12.8075306831972, (1, 200): 12.555993749453744, (2, 8): 8.68254095475854, (2, 3): 1, (2, 7): 8.810372482122368, (2, 200): 5.04196737467203, (3, 4): 9.388249470739549, (3, 5): 1, (3, 8): 2.7333233462461095, (4, 7): 9.963363442809428, (4, 8): 11.0856978036655, (4, 5): 6.223422899900715, (5, 200): 8.099368501732235, (6, 200): 12.249741800610945, (6, 7): 8.002525614869997}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 9.291828936810017, 'r1': 9.318656004673107}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 8.21338102319847, 'o1': 5.149100820257338}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1']}

    state.loc = { 'r0': 200, 'r1': 2, 'm0': 200, 'm1': 2, 'p0': 4, 'o0': 2, 'o1': 2,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 5, 'm1': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}