__author__ = 'patras'
from domain_chargeableRobot import *
from timer import DURATION
from state import state

DURATION.TIME = {
    'put': 2,
    'take': 2,
    'perceive': 2,
    'charge': 2,
    'move': 2,
    'moveToEmergency': 2,
    'moveCharger': 2,
    'addressEmergency': 2,
    'wait': 2,
}

DURATION.COUNTER = {
    'put': 2,
    'take': 2,
    'perceive': 2,
    'charge': 2,
    'move': 2,
    'moveToEmergency': 2,
    'moveCharger': 2,
    'addressEmergency': 2,
    'wait': 2,
}

rv.LOCATIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rv.EDGES = {1: [7], 2: [8], 3: [8], 4: [8, 9], 5: [7], 6: [7], 7: [1, 5, 6, 8], 8: [2, 3, 4, 7], 9: [4, 10], 10: [9]}
rv.OBJECTS=['o1']

rv.ROBOTS=['r1','r2']

def ResetState():
    state.loc = {'r1': 3, 'r2': 1}
    state.charge = {'r1': 3, 'r2': 3}
    state.load = {'r1': NIL, 'r2': NIL}
    state.pos = {'c1': 'r2', 'o1': 5}
    state.containers = { 1:[],2:[],3:[],4:[],5:['o1'],6:[],7:[],8:[],9:[],10:[],}
    state.emergencyHandling = {'r1': False, 'r2': False}
    state.view = {}
    for l in rv.LOCATIONS:
        state.view[l] = False

tasks = {
    1: [['fetch', 'r1', 'o1']],
    3: [['emergency', 'r1', 2, 1]],
}
eventsEnv = {
}