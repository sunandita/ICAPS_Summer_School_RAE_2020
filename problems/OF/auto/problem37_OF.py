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

rv.LOCATIONS = [0, 1, 2, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 200, 2], 1: [2, 0, 200], 2: [0, 1], 200: [1, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 6.555628528029137, (0, 200): 6.861349742329227, (0, 2): 12.5437683321513, (1, 2): 10.957872340617792, (1, 200): 4.4516625178176845}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.776182053377536, 'r1': 7.4761600290009005}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True,  'o7': True,  'o8': True,  'o9': True,  'o10': True,  'o11': True, }
    state.OBJ_WEIGHT = {'o0': 5.313950194948335, 'o1': 5.320806893169291, 'o2': 5.178851533788255, 'o3': 7.210305746530598, 'o4': 7.4664182856328445, 'o5': 7.4761600290009005, 'o6': 7.4761600290009005, 'o7': 6.269069606733101, 'o8': 5.335701742978909, 'o9': 7.4761600290009005, 'o10': 7.4761600290009005, 'o11': 5.9822945089705195}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2', 'o3'], 'type1': ['o4'], 'type2': ['o5'], 'type3': ['o6', 'o7'], 'type4': ['o8', 'o9', 'o10', 'o11']}

    state.loc = { 'r0': 2, 'r1': 0, 'm0': 0, 'm1': 0, 'p0': 200, 'o0': 2, 'o1': 2, 'o2': 1, 'o3': 0, 'o4': 0, 'o5': 200, 'o6': 0, 'o7': 1, 'o8': 1, 'o9': 200, 'o10': 0, 'o11': 2,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 5, 'm1': 6}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    4: [['orderStart', ['type0']]],
    6: [['orderStart', ['type0']]],
}
eventsEnv = {
}