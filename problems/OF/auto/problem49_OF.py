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

rv.LOCATIONS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 200]
rv.FACTORY1 = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 200})
rv.FACTORY_UNION = rv.FACTORY1
rv.SHIPPING_DOC = {rv.FACTORY1: 6}

rv.GROUND_EDGES = {0: [3, 4, 5, 6, 7, 200], 1: [4, 5, 8], 2: [3, 4], 3: [0, 2], 4: [0, 1, 2, 5], 5: [0, 1, 4, 6, 7, 8], 6: [0, 200, 5], 7: [0, 5], 8: [1, 5], 200: [0, 6]}
rv.GROUND_WEIGHTS = {(0, 3): 11.105215143677352, (0, 4): 1, (0, 5): 3.408671374651795, (0, 6): 12.606580779469017, (0, 7): 3.1959532510968636, (0, 200): 6.1270006465458335, (1, 4): 7.078056418073309, (1, 5): 5.073187697202297, (1, 8): 9.997626386634341, (2, 3): 9.281204458289137, (2, 4): 11.973380206797469, (4, 5): 3.0290035722666726, (5, 6): 8.873039846734885, (5, 7): 7.231832525039564, (5, 8): 2.129548935261343, (6, 200): 8.958139452794645}

rv.ROBOTS = { 'r0': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 4.5295268628395196}
rv.MACHINES = { 'm0': rv.FACTORY1,  'm1': rv.FACTORY1, }
rv.PALLETS = { 'p0', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True,  'o3': True,  'o4': True, }
    state.OBJ_WEIGHT = {'o0': 4.5295268628395196, 'o1': 4.5295268628395196, 'o2': 4.5295268628395196, 'o3': 4.5295268628395196, 'o4': 4.5295268628395196}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1'], 'type2': ['o2', 'o3', 'o4']}

    state.loc = { 'r0': 5, 'm0': 3, 'm1': 0, 'p0': 3, 'o0': 2, 'o1': 2, 'o2': 7, 'o3': 8, 'o4': 5,}
    state.load = { 'r0': NIL,}
    state.busy = {'r0': False, 'm0': False, 'm1': False}
    state.numUses = {'m0': 12, 'm1': 3}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    1: [['orderStart', ['type1']]],
    2: [['orderStart', ['type2']]],
}
eventsEnv = {
}