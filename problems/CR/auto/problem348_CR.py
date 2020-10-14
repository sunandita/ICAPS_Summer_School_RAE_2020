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

rv.LOCATIONS = [1, 2, 3, 4]
rv.EDGES = {1: [3], 2: [3], 3: [1, 2, 4], 4: [3]}
rv.OBJECTS=['o1']

rv.ROBOTS=['r1']

def ResetState():
    state.loc = {'r1': 2}
    state.charge = {'r1': 3}
    state.load = {'r1': NIL}
    state.pos = {'c1': 1, 'o1': UNK}
    state.containers = { 1:[],2:['o1'],3:[],4:[],}
    state.emergencyHandling = {'r1': False, 'r2': False}
    state.view = {}
    for l in rv.LOCATIONS:
        state.view[l] = False

tasks = {
    4: [['fetch', 'r1', 'o1']],
}
eventsEnv = {
}