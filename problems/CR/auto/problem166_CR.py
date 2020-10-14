__author__ = 'patras'
from domain_chargeableRobot import *
from timer import DURATION
from state import state

DURATION.TIME = {
    'put': 2,
    'take': 2,
    'perceive': 3,
    'charge': 5,
    'move': 10,
    'moveToEmergency': 5,
    'moveCharger': 15,
    'addressEmergency': 10,
    'wait': 5,
}

DURATION.COUNTER = {
    'put': 2,
    'take': 2,
    'perceive': 3,
    'charge': 5,
    'move': 10,
    'moveToEmergency': 5,
    'moveCharger': 15,
    'addressEmergency': 10,
    'wait': 5,
}

rv.LOCATIONS = [1, 2, 3, 4]
rv.EDGES = {1: [3], 2: [3], 3: [1, 2, 4], 4: [3]}
rv.OBJECTS=['o1']

rv.ROBOTS=['r1','r2']

def ResetState():
    state.loc = {'r1': 3, 'r2': 1}
    state.charge = {'r1': 2, 'r2': 3}
    state.load = {'r1': NIL, 'r2': NIL}
    state.pos = {'c1': 'r2', 'o1': 1}
    state.containers = { 1:['o1'],2:[],3:[],4:[],}
    state.emergencyHandling = {'r1': False, 'r2': False}
    state.view = {}
    for l in rv.LOCATIONS:
        state.view[l] = False

tasks = {
    6: [['fetch', 'r1', 'o1']],
}
eventsEnv = {
}