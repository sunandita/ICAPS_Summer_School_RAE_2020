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
rv.SHIPPING_DOC = {rv.FACTORY1: 4}

rv.GROUND_EDGES = {0: [1, 4], 1: [0, 2, 5, 6], 2: [1, 3, 5, 6, 200], 3: [4, 2], 4: [0, 200, 3, 5], 5: [4, 6, 1, 2], 6: [1, 2, 5], 200: [2, 4]}
rv.GROUND_WEIGHTS = {(0, 1): 1.5811258496574823, (0, 4): 12.848162845330396, (1, 2): 4.286026679315222, (1, 5): 11.149564973668122, (1, 6): 4.179870880775381, (2, 3): 3.6211211779444037, (2, 5): 5.648916254189767, (2, 6): 16.35193662765026, (2, 200): 1, (3, 4): 5.5795169560647295, (4, 200): 10.23030478260726, (4, 5): 10.698194133839182, (5, 6): 10.863130298402348}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.8266374100587095}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True, }
    state.OBJ_WEIGHT = {'o0': 4.8266374100587095, 'o1': 4.8266374100587095, 'o2': 4.471734117207381, 'o3': 3.644095969020852, 'o4': 4.8266374100587095, 'o5': 4.385114072957267}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3', 'o4', 'o5']}

    state.loc = { 'r0': 1, 'm0': 4, 'm1': 2, 'm2': 6, 'p0': 2, 'p1': 1, 'o0': 6, 'o1': 200, 'o2': 0, 'o3': 5, 'o4': 2, 'o5': 200,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 8, 'm1': 9, 'm2': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}