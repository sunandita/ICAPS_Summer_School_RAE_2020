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
rv.SHIPPING_DOC = {rv.FACTORY1: 1}

rv.GROUND_EDGES = {0: [5], 1: [2, 4, 200, 5], 2: [5, 1, 3, 200], 3: [2], 4: [5, 1], 5: [0, 1, 2, 4], 200: [2, 1]}
rv.GROUND_WEIGHTS = {(0, 5): 8.362213045007262, (1, 2): 5.062753777913743, (1, 4): 7.545266832793395, (1, 200): 13.27423474395783, (1, 5): 13.178100768759261, (2, 5): 8.046627845893962, (2, 3): 15.0657375784944, (2, 200): 11.262941868923955, (4, 5): 13.26780386637843}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 10.429419358150168, 'r1': 6.600643225056278, 'r2': 6.234403940226066}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True, }
    state.OBJ_WEIGHT = {'o0': 9.223145008161694, 'o1': 3.8021173966833803, 'o2': 5.82836407998862, 'o3': 4.695430198636432, 'o4': 8.863490400564952, 'o5': 5.071658267536914}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2', 'o3', 'o4', 'o5']}

    state.loc = { 'r0': 0, 'r1': 1, 'r2': 2, 'm0': 5, 'p0': 0, 'o0': 200, 'o1': 0, 'o2': 4, 'o3': 0, 'o4': 0, 'o5': 2,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'm0': False}
    state.numUses = {'m0': 6}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    2: [['orderStart', ['type0']]],
}
eventsEnv = {
}