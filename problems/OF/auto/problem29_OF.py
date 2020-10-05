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
rv.SHIPPING_DOC = {rv.FACTORY1: 6}

rv.GROUND_EDGES = {0: [3, 5, 7, 2, 6], 1: [3, 6, 4], 2: [0, 5, 200], 3: [4, 7, 0, 1, 6, 200], 4: [1, 3, 5], 5: [0, 2, 6, 4], 6: [0, 3, 200, 1, 5], 7: [3, 0], 200: [2, 3, 6]}
rv.GROUND_WEIGHTS = {(0, 3): 14.698382858944546, (0, 5): 5.33202549909805, (0, 7): 10.714032192767828, (0, 2): 8.209512575148201, (0, 6): 8.72335607373077, (1, 3): 14.864594022485123, (1, 6): 3.317473420265001, (1, 4): 3.985917036363583, (2, 5): 9.345645129758214, (2, 200): 7.377484773471038, (3, 4): 8.917631121979175, (3, 7): 6.235522156715584, (3, 6): 7.126849883993092, (3, 200): 11.30340049821606, (4, 5): 3.253905813006484, (5, 6): 16.828715613793, (6, 200): 7.2590437451523595}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.145068250830962}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1,  'm4': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 6.145068250830962, 'o1': 6.145068250830962, 'o2': 6.145068250830962, 'o3': 6.145068250830962}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 4, 'm0': 1, 'm1': 3, 'm2': 0, 'm3': 7, 'm4': 2, 'p0': 3, 'o0': 6, 'o1': 2, 'o2': 4, 'o3': 0,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False, 'm4': False}
    state.numUses = {'m0': 14, 'm1': 6, 'm2': 9, 'm3': 10, 'm4': 8}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    3: [['orderStart', ['type0']]],
}
eventsEnv = {
}