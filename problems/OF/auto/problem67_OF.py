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

rv.LOCATIONS = [0, 1, 2, 3, 4, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [3, 4, 200], 1: [2, 3, 4], 2: [4, 1, 3, 200], 3: [0, 2, 4, 200, 1], 4: [0, 1, 2, 3], 200: [0, 2, 3]}
rv.GROUND_WEIGHTS = {(0, 3): 13.352859308830524, (0, 4): 5.046970186538651, (0, 200): 10.010961944167198, (1, 2): 3.0308010806785823, (1, 3): 3.329391587877228, (1, 4): 5.29404776705175, (2, 4): 6.939252710716521, (2, 3): 10.224313957877115, (2, 200): 8.243972290296863, (3, 4): 12.280345302378747, (3, 200): 8.937118065703686}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 10.707076102461777, 'r1': 6.500827573868887}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True, }
    state.OBJ_WEIGHT = {'o0': 4.962526079874616, 'o1': 6.181556014465999, 'o2': 7.955699526114469, 'o3': 10.165052997635312, 'o4': 6.45389336041057, 'o5': 5.132547235244778, 'o6': 6.6724572103218796}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1'], 'type2': ['o2', 'o3', 'o4', 'o5', 'o6']}

    state.loc = { 'r0': 200, 'r1': 1, 'm0': 200, 'm1': 3, 'p0': 3, 'p1': 200, 'o0': 3, 'o1': 0, 'o2': 4, 'o3': 1, 'o4': 0, 'o5': 1, 'o6': 3,}
    state.load = { 'r0': NIL, 'r1': NIL,}
    state.busy = {'r0': False, 'r1': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 19, 'm1': 10}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    7: [['orderStart', ['type0']]],
    4: [['orderStart', ['type1']]],
}
eventsEnv = {
}