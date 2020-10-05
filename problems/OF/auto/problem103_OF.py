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

rv.GROUND_EDGES = {0: [1, 4, 5], 1: [0, 200, 2, 4], 2: [1, 3, 4], 3: [4, 2], 4: [0, 1, 2, 3], 5: [0], 200: [1]}
rv.GROUND_WEIGHTS = {(0, 1): 11.517199427949283, (0, 4): 9.301872791589005, (0, 5): 9.928368048672654, (1, 200): 7.175713994702222, (1, 2): 8.781683778617813, (1, 4): 2.178045001056484, (2, 3): 12.229348218293875, (2, 4): 10.162719124650032, (3, 4): 7.061430096770288}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 5.067878880593362}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True,  'o7': True,  'o8': True, }
    state.OBJ_WEIGHT = {'o0': 5.067878880593362, 'o1': 5.067878880593362, 'o2': 5.067878880593362, 'o3': 5.067878880593362, 'o4': 5.067878880593362, 'o5': 5.067878880593362, 'o6': 5.067878880593362, 'o7': 5.067878880593362, 'o8': 5.067878880593362}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2'], 'type2': ['o3', 'o4', 'o5', 'o6', 'o7', 'o8']}

    state.loc = { 'r0': 5, 'm0': 5, 'm1': 5, 'p0': 0, 'o0': 5, 'o1': 3, 'o2': 2, 'o3': 5, 'o4': 3, 'o5': 1, 'o6': 0, 'o7': 0, 'o8': 1,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 12, 'm1': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    4: [['orderStart', ['type0']]],
    5: [['orderStart', ['type0']]],
}
eventsEnv = {
}