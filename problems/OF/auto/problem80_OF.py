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

rv.GROUND_EDGES = {0: [5, 6, 3], 1: [5, 7], 2: [5, 200, 3, 6], 3: [0, 2, 5], 4: [5], 5: [4, 0, 1, 2, 3, 200], 6: [0, 2, 7, 200], 7: [1, 6], 200: [5, 6, 2]}
rv.GROUND_WEIGHTS = {(0, 5): 7.9850546018862145, (0, 6): 6.9468710812757815, (0, 3): 12.099718445874334, (1, 5): 7.528748667927151, (1, 7): 6.418070736597217, (2, 5): 2.638611160543803, (2, 200): 7.8118804436721145, (2, 3): 3.9268270102333664, (2, 6): 10.6254313640586, (3, 5): 5.469893763260881, (4, 5): 5.862988480314365, (5, 200): 7.930686919202043, (6, 7): 11.9166581376803, (6, 200): 7.026333797476917}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.295545079301372}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True,  'o5': True,  'o6': True,  'o7': True, }
    state.OBJ_WEIGHT = {'o0': 6.707214929077857, 'o1': 6.448795041001162, 'o2': 5.54703539784075, 'o3': 7.295545079301372, 'o4': 6.655084061734898, 'o5': 7.295545079301372, 'o6': 7.235373845668021, 'o7': 4.7440365198981445}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2', 'o3', 'o4', 'o5', 'o6'], 'type2': ['o7']}

    state.loc = { 'r0': 4, 'm0': 6, 'p0': 0, 'p1': 3, 'o0': 4, 'o1': 7, 'o2': 5, 'o3': 200, 'o4': 200, 'o5': 4, 'o6': 200, 'o7': 5,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False}
    state.numUses = {'m0': 10}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    3: [['orderStart', ['type0']]],
    8: [['orderStart', ['type1']]],
}
eventsEnv = {
}