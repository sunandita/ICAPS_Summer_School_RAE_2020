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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 4, 200, 2, 3], 1: [0, 2, 200], 2: [0, 1, 3, 4, 200], 3: [0, 2, 4], 4: [2, 3, 0], 200: [1, 2, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 18.853589096101405, (0, 4): 7.430004739270858, (0, 200): 6.7608221665783494, (0, 2): 4.071858535009774, (0, 3): 4.541860352906035, (1, 2): 3.5921113629947357, (1, 200): 9.145130695277286, (2, 3): 7.287999174903218, (2, 4): 9.541198508083502, (2, 200): 6.476948628778672, (3, 4): 4.55086595540152}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.305679811916985, 'r1': 10.887778219430881}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1,  'm4': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 6.080400311491626, 'o1': 7.295326104242323, 'o2': 3.887474478915579}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1'], 'type2': ['o2']}

    state.loc = { 'r0': 4, 'r1': 200, 'm0': 0, 'm1': 0, 'm2': 3, 'm3': 0, 'm4': 200, 'p0': 1, 'p1': 200, 'o0': 200, 'o1': 0, 'o2': 4,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False, 'm4': False}
    state.numUses = {'m0': 8, 'm1': 10, 'm2': 16, 'm3': 12, 'm4': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}