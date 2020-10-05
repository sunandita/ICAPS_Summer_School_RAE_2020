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
rv.SHIPPING_DOC = {rv.FACTORY1: 2}

rv.GROUND_EDGES = {0: [3, 7, 2, 200], 1: [5], 2: [0, 200, 4, 5], 3: [0, 5], 4: [2, 7], 5: [2, 3, 7, 1], 6: [7], 7: [6, 0, 4, 5, 200], 200: [0, 7, 2]}
rv.GROUND_WEIGHTS = {(0, 3): 12.100828445662533, (0, 7): 10.786771690054938, (0, 2): 6.354918741396784, (0, 200): 8.631422180000296, (1, 5): 6.187779675607602, (2, 200): 15.481107043463831, (2, 4): 1.3573799808668152, (2, 5): 6.08379926192124, (3, 5): 4.010517598386566, (4, 7): 18.147032066161714, (5, 7): 6.6276965546545155, (6, 7): 8.21482710014791, (7, 200): 16.183822810669312}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.34475755121495, 'r1': 10.110128872725488, 'r2': 5.77995515100151}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True, }
    state.OBJ_WEIGHT = {'o0': 7.831038148980504, 'o1': 5.84861540324271, 'o2': 2.0302124179080305, 'o3': 7.216938517475796, 'o4': 5.779493503259726, 'o5': 6.370797079715744, 'o6': 5.2002039098416395}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1'], 'type2': ['o2', 'o3', 'o4', 'o5', 'o6']}

    state.loc = { 'r0': 4, 'r1': 7, 'r2': 7, 'm0': 3, 'p0': 4, 'o0': 3, 'o1': 6, 'o2': 3, 'o3': 5, 'o4': 4, 'o5': 0, 'o6': 5,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'm0': False}
    state.numUses = {'m0': 11}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}