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
rv.SHIPPING_DOC = {rv.FACTORY1: 2}

rv.GROUND_EDGES = {0: [4, 3, 6, 200], 1: [2, 3, 4, 6, 5], 2: [3, 6, 200, 1], 3: [0, 1, 2, 4], 4: [3, 5, 0, 1], 5: [1, 6, 4], 6: [0, 1, 2, 5], 200: [0, 2]}
rv.GROUND_WEIGHTS = {(0, 4): 8.447581477764585, (0, 3): 6.194729459785743, (0, 6): 4.83163164044659, (0, 200): 10.267926085851485, (1, 2): 4.3947090805945646, (1, 3): 1, (1, 4): 3.8605513342817863, (1, 6): 3.958352673559964, (1, 5): 14.359560174339432, (2, 3): 1.3715131522485962, (2, 6): 5.275100921381091, (2, 200): 2.9582779134432275, (3, 4): 1, (4, 5): 3.7044854063452437, (5, 6): 8.299969473277063}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 6.617776338252326, 'r1': 6.970557963186356, 'r2': 5.889511037237499}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 4.982164816682058, 'o1': 3.650618229766755, 'o2': 6.970557963186356, 'o3': 6.970557963186356, 'o4': 6.970557963186356}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2', 'o3'], 'type2': ['o4']}

    state.loc = { 'r0': 3, 'r1': 4, 'r2': 200, 'm0': 0, 'p0': 200, 'p1': 0, 'p2': 2, 'o0': 3, 'o1': 1, 'o2': 4, 'o3': 200, 'o4': 4,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'm0': False}
    state.numUses = {'m0': 12}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type2']]],
}
eventsEnv = {
}