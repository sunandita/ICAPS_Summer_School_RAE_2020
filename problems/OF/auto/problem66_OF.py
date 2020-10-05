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

rv.GROUND_EDGES = {0: [1, 200], 1: [0, 2, 4, 5, 6, 200], 2: [3, 5, 1, 4, 200], 3: [2, 4], 4: [2, 3, 5, 1, 6], 5: [2, 6, 1, 4], 6: [1, 4, 5], 200: [1, 2, 0]}
rv.GROUND_WEIGHTS = {(0, 1): 8.89582635350458, (0, 200): 1.7110526195253986, (1, 2): 12.137113595173947, (1, 4): 10.600094999901517, (1, 5): 10.300143898643881, (1, 6): 10.561568917682504, (1, 200): 1, (2, 3): 8.467929892387122, (2, 5): 10.996268674559927, (2, 4): 9.329353212574459, (2, 200): 11.37379364628414, (3, 4): 9.626751853161075, (4, 5): 10.965770916732556, (4, 6): 3.663508370712429, (5, 6): 9.552106506430276}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.869994352779302, 'r1': 4.831003817987641, 'r2': 6.6638820237057645, 'r3': 8.759976038554091}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True, }
    state.OBJ_WEIGHT = {'o0': 4.906925666706037}
    state.OBJ_CLASS = {'type0': ['o0']}

    state.loc = { 'r0': 2, 'r1': 4, 'r2': 1, 'r3': 6, 'm0': 1, 'p0': 3, 'p1': 3, 'p2': 4, 'o0': 5,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'm0': False}
    state.numUses = {'m0': 5}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}