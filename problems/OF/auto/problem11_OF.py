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

rv.LOCATIONS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 3}

rv.GROUND_EDGES = {0: [2, 5, 6, 7, 8, 9], 1: [3, 8, 9, 2], 2: [1, 0], 3: [6, 9, 200, 1], 4: [6, 9, 8], 5: [8, 0, 200], 6: [0, 3, 4], 7: [9, 0, 200], 8: [0, 4, 5, 1], 9: [0, 1, 3, 4, 7], 200: [3, 5, 7]}
rv.GROUND_WEIGHTS = {(0, 2): 11.836227908229727, (0, 5): 6.497580288297422, (0, 6): 7.998864041137603, (0, 7): 2.936339427455838, (0, 8): 11.05402743630566, (0, 9): 14.653383120309964, (1, 3): 6.929771348678841, (1, 8): 13.418669089103666, (1, 9): 9.53567596979952, (1, 2): 9.225953342649188, (3, 6): 4.60001424645597, (3, 9): 9.413358603365012, (3, 200): 8.040631424758427, (4, 6): 7.1096886187898924, (4, 9): 6.000721413434702, (4, 8): 11.656303501965445, (5, 8): 11.599805975707715, (5, 200): 9.296080739523108, (7, 9): 12.602538563869187, (7, 200): 3.850067420380298}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 10.135556703548975}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1,  'm2': rv.FACTORY1,  'm3': rv.FACTORY1,  'm4': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True, }
    state.OBJ_WEIGHT = {'o0': 6.274037753793541, 'o1': 5.47564767170286, 'o2': 6.366043418136403, 'o3': 8.347417119497342}
    state.OBJ_CLASS = {'type0': ['o0', 'o1'], 'type1': ['o2', 'o3']}

    state.loc = { 'r0': 0, 'm0': 3, 'm1': 200, 'm2': 1, 'm3': 5, 'm4': 9, 'p0': 1, 'p1': 2, 'p2': 6, 'o0': 9, 'o1': 200, 'o2': 8, 'o3': 9,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False, 'm2': False, 'm3': False, 'm4': False}
    state.numUses = {'m0': 9, 'm1': 11, 'm2': 10, 'm3': 9, 'm4': 8}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type0']]],
}
eventsEnv = {
}