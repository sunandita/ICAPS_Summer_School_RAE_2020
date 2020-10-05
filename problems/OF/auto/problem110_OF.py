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
rv.SHIPPING_DOC = {rv.FACTORY1: 1}

rv.GROUND_EDGES = {0: [3, 1, 2, 200], 1: [0, 200, 3], 2: [0, 3], 3: [0, 1, 2], 200: [0, 1]}
rv.GROUND_WEIGHTS = {(0, 3): 4.741440558543934, (0, 1): 4.469824494313471, (0, 2): 13.697003668532858, (0, 200): 6.459476006485116, (1, 200): 11.634966288417107, (1, 3): 5.7100967770873785, (2, 3): 8.632019929240215}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.844914272144662, 'r1': 9.906407869276464}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 6.93227260974876, 'o1': 5.086924113005167, 'o2': 6.430727613737984, 'o3': 7.980678479409873}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3']}

    state.loc = { 'r0': 2, 'r1': 1, 'm0': 1, 'm1': 3, 'p0': 0, 'p1': 0, 'o0': 2, 'o1': 2, 'o2': 200, 'o3': 200,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 2, 'm1': 13}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}