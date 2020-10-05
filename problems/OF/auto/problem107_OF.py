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
rv.SHIPPING_DOC = {rv.FACTORY1: 0}

rv.GROUND_EDGES = {0: [2, 200, 3, 4], 1: [2, 3], 2: [4, 0, 1, 200], 3: [0, 1, 4, 200], 4: [0, 2, 3], 200: [2, 3, 0]}
rv.GROUND_WEIGHTS = {(0, 2): 3.933132164125576, (0, 200): 3.3738969412898934, (0, 3): 12.449231595143372, (0, 4): 12.778381208802212, (1, 2): 12.050680270184595, (1, 3): 10.134513193914595, (2, 4): 6.891027767025113, (2, 200): 2.915883557352087, (3, 4): 5.096640486085088, (3, 200): 12.68643391413444}

rv.ROBOTS = { 'r0': rv.FACTORY1,  'r1': rv.FACTORY1,  'r2': rv.FACTORY1,  'r3': rv.FACTORY1,  'r4': rv.FACTORY1, }
rv.ROBOT_CAPACITY = {'r0': 9.005158456111172, 'r1': 6.526343179880396, 'r2': 5.836534042017294, 'r3': 8.453668448048779, 'r4': 9.38806910019131}
rv.MACHINES = { 'm0': rv.FACTORY1, }
rv.PALLETS = { 'p0',  'p1', }


def ResetState():
    state.OBJECTS = { 'o0': True,  'o1': True,  'o2': True, }
    state.OBJ_WEIGHT = {'o0': 7.605141330245276, 'o1': 6.770318628414375, 'o2': 5.424459341264589}
    state.OBJ_CLASS = {'type0': ['o0'], 'type1': ['o1', 'o2']}

    state.loc = { 'r0': 3, 'r1': 1, 'r2': 200, 'r3': 0, 'r4': 200, 'm0': 3, 'p0': 2, 'p1': 1, 'o0': 4, 'o1': 200, 'o2': 2,}
    state.load = { 'r0': NIL, 'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL,}
    state.busy = {'r0': False, 'r1': False, 'r2': False, 'r3': False, 'r4': False, 'm0': False}
    state.numUses = {'m0': 9}
    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}
    state.shouldRedo = {}

tasks = {
    5: [['orderStart', ['type0']]],
    2: [['orderStart', ['type1']]],
}
eventsEnv = {
}