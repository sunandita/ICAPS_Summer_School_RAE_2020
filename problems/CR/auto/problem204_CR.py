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

rv.LOCATIONS = [1, 2, 3, 4, 5, 6, 7, 8]
rv.EDGES = {1: [7], 2: [8], 3: [8], 4: [8], 5: [7], 6: [7], 7: [1, 5, 6, 8], 8: [2, 3, 4, 7]}
rv.OBJECTS=['o1']

rv.ROBOTS=['r1']

def ResetState():
    state.loc = {'r1': 2}
    state.charge = {'r1': 2}
    state.load = {'r1': NIL}
    state.pos = {'c1': 1, 'o1': UNK}
    state.containers = { 1:[],2:[],3:['o1'],4:[],5:[],6:[],7:[],8:[],}
    state.emergencyHandling = {'r1': False, 'r2': False}
    state.view = {}
    for l in rv.LOCATIONS:
        state.view[l] = False

tasks = {
    1: [['fetch', 'r1', 'o1']],
}
eventsEnv = {
}