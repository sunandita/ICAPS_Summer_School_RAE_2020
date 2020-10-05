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
rv.SHIPPING_DOC = {rv.FACTORY1: 6}

rv.GROUND_EDGES = {0: [1, 2, 3, 4], 1: [0, 2], 2: [0, 1, 3, 4], 3: [0, 4, 2, 5, 6, 7, 200], 4: [0, 2, 3], 5: [3, 7], 6: [3, 200], 7: [3, 5], 200: [3, 6]}
rv.GROUND_WEIGHTS = {(0, 1): 7.700109661175884, (0, 2): 2.2780598918360475, (0, 3): 20.084326548670802, (0, 4): 7.291858696555021, (1, 2): 1, (2, 3): 1, (2, 4): 5.452808344590219, (3, 4): 9.153964228531322, (3, 5): 8.908300635419154, (3, 6): 5.052341665510067, (3, 7): 5.220638612951001, (3, 200): 12.37825205387216, (5, 7): 5.108299608991839, (6, 200): 11.078189097411867}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1,  'r4': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 7.899300389602575, 'r1': 5.0730275092512365, 'r2': 8.646200556050937, 'r3': 6.7990910836691745, 'r4': 8.383173900440362}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1',  'p2', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True, }
    state.OBJ_WEIGHT = {'o0': 5.942863227490383, 'o1': 5.114093467067327}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1']}

    state.loc = { 'r0': 7, 'r1': 2, 'r2': 6, 'r3': 4, 'r4': 6, 'm0': 3, 'm1': 4, 'p0': 7, 'p1': 3, 'p2': 200, 'o0': 6, 'o1': 6,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'r4': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 10, 'm1': 5}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type1']]],
}
eventsEnv = {
}