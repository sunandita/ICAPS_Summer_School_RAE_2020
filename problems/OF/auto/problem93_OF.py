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
rv.SHIPPING_DOC = {rv.FACTORY1: 2}

rv.GROUND_EDGES = {0: [2, 1, 3, 200], 1: [0], 2: [4, 200, 0], 3: [0, 4, 200], 4: [3, 2], 200: [0, 3, 2]}
rv.GROUND_WEIGHTS = {(0, 2): 5.189585276358512, (0, 1): 8.075731661406682, (0, 3): 7.491885779726273, (0, 200): 10.689843290644609, (2, 4): 12.617903092719871, (2, 200): 9.448696610223115, (3, 4): 12.50510834065409, (3, 200): 5.0528529292682}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 5.263994006880802, 'r1': 7.247098661677207, 'r2': 8.12734044066581, 'r3': 9.14722082027056}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 7.104340223004195, 'o1': 5.180779293723558}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1']}

    state.loc = { 'r0': 4, 'r1': 1, 'r2': 200, 'r3': 2, 'm0': 200, 'p0': 4, 'p1': 200, 'p2': 4, 'o0': 2, 'o1': 2,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False}
    state.numUses = {'m0': 8}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
    3: [['orderStart', ['type1']]],
}
eventsEnv = {
}