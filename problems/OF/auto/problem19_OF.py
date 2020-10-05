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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 5, 200, 2, 4], 1: [2, 4, 5, 0, 3, 200], 2: [0, 1, 4, 5], 3: [1], 4: [0, 1, 2, 5], 5: [1, 2, 0, 4], 200: [1, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 6.499229647088665, (0, 5): 2.692119274311481, (0, 200): 6.2181264795712705, (0, 2): 7.121374187150064, (0, 4): 7.908766557240531, (1, 2): 10.484258297196071, (1, 4): 2.8722782433551934, (1, 5): 4.117098308924607, (1, 3): 7.129538742746605, (1, 200): 8.245597546318098, (2, 4): 9.026732394538875, (2, 5): 5.704832854262499, (4, 5): 11.599770968738499}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.599413029987371}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True, }
    state.OBJ_WEIGHT = {'o0': 4.599413029987371, 'o1': 4.599413029987371, 'o2': 3.4035481992311962, 'o3': 4.599413029987371, 'o4': 4.599413029987371, 'o5': 4.599413029987371, 'o6': 4.599413029987371}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2'], 'type2': ['o3', 'o4', 'o5', 'o6']}

    state.loc = { 'r0': 1, 'm0': 5, 'm1': 4, 'm2': 1, 'p0': 2, 'p1': 1, 'p2': 200, 'o0': 200, 'o1': 3, 'o2': 4, 'o3': 200, 'o4': 0, 'o5': 200, 'o6': 0,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False}
    state.numUses = {'m0': 10, 'm1': 13, 'm2': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    4: [['orderStart', ['type0']]],
    6: [['orderStart', ['type0']]],
}
eventsEnv = {
}