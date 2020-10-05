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
rv.SHIPPING_DOC = {rv.FACTORY1: 4}

rv.GROUND_EDGES = {0: [3, 4, 5, 1, 7], 1: [0, 3, 6, 200], 2: [4, 200], 3: [1, 5, 0], 4: [2, 5, 200, 0], 5: [0, 3, 4], 6: [1], 7: [0], 200: [1, 2, 4]}
rv.GROUND_WEIGHTS = {(0, 3): 8.791204719746721, (0, 4): 1, (0, 5): 15.097203108418617, (0, 1): 11.319727572860847, (0, 7): 7.4428758660017085, (1, 3): 10.162926817229664, (1, 6): 14.549205867308947, (1, 200): 8.198707994258585, (2, 4): 7.6816361780419005, (2, 200): 16.0231974633462, (3, 5): 3.134786161130317, (4, 5): 4.791350932900812, (4, 200): 9.244489086131582}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 8.34877119294901, 'r1': 5.486798055561971, 'r2': 10.368918051760417, 'r3': 7.622172685719587}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 6.988422249348128}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 5, 'r1': 6, 'r2': 1, 'r3': 1, 'm0': 4, 'm1': 0, 'm2': 2, 'p0': 200, 'p1': 6, 'p2': 1, 'o0': 7,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 8, 'm1': 12, 'm2': 12}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}