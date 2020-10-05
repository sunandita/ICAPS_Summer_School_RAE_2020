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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [1, 200, 3, 4, 5], 1: [0, 4, 6], 2: [5, 3], 3: [0, 2, 5], 4: [0, 1, 5, 6, 200], 5: [0, 3, 2, 4, 200], 6: [1, 4], 200: [4, 5, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 9.72754351934888, (0, 200): 8.739316785757408, (0, 3): 8.195113524249901, (0, 4): 9.876646571902558, (0, 5): 4.098771110320094, (1, 4): 5.6733850576627125, (1, 6): 4.623778012558674, (2, 5): 10.2141988439455, (2, 3): 1, (3, 5): 7.108814502296398, (4, 5): 9.871901869533751, (4, 6): 4.5347146005410055, (4, 200): 3.9096914893936887, (5, 200): 8.40914949638789}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 11.634501011224211}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 5.189611504345837, 'o1': 7.608576843392303, 'o2': 3.096734212097397, 'o3': 6.015695447906999, 'o4': 5.168065961767085}
    state.OBJ_CLASS = {'type0': ['o0', 'o1', 'o2'], 'type1': ['o3'], 'type2': ['o4']}

    state.loc = { 'r0': 5, 'm0': 6, 'p0': 0, 'p1': 200, 'o0': 1, 'o1': 3, 'o2': 2, 'o3': 0, 'o4': 3,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 6}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    5: [['orderStart', ['type0']]],
    3: [['orderStart', ['type0']]],
}
eventsEnv = {
}