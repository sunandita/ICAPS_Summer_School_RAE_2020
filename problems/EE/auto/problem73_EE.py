__author__ = 'patras'
from domain_exploreEnv import *
from timer import DURATION
from state import state, rv

DURATION.TIME = {
    'survey': 5,
    'monitor': 5,
    'screen': 5,
    'sample': 5,
    'process': 5,
    'fly': 3,
    'deposit': 1,
    'transferData': 1,
    'take': 2,
    'put': 2,
    'move': 10,
    'charge': 5,
    'negotiate': 5,
    'handleAlien': 5,
}

DURATION.COUNTER = {
    'survey': 5,
    'monitor': 5,
    'screen': 5,
    'sample': 5,
    'process': 5,
    'fly': 3,
    'deposit': 1,
    'transferData': 1,
    'take': 2,
    'put': 2,
    'move': 10,
    'charge': 5,
    'negotiate': 5,
    'handleAlien': 5,
}

rv.TYPE = {'e1': 'survey', 'e2': 'monitor', 'e3': 'screen', 'e4': 'sample', 'e5':'process'}
rv.EQUIPMENT = {'survey': 'e1', 'monitor': 'e2', 'screen': 'e3', 'sample': 'e4', 'process': 'e5'}
rv.EQUIPMENTTYPE = {'e1': 'survey', 'e2': 'monitor', 'e3': 'screen', 'e4': 'sample', 'e5':'process'}
rv.LOCATIONS = ['base', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6']
rv.EDGES = {'base': {'z1': 50, 'z3': 50, 'z4': 40, 'z6': 40}, 'z1': {'base': 50, 'z2': 20}, 'z2': {'z1': 20, 'z3': 20}, 'z3': {'z2': 20, 'base': 50}, 'z4': {'z3': 90, 'z5': 35}, 'z5': {'z4': 35, 'z6': 35}, 'z6': {'base': 40, 'z5': 35}}

def ResetState():
    state.loc = {'r1': 'base', 'r2': 'base', 'UAV': 'base'}
    state.charge = { 'UAV': 80, 'r1': 50, 'r2': 80}
    state.data = { 'UAV': 1, 'r1': 3, 'r2': 1}
    state.pos = {'c1': 'base', 'e1': 'base', 'e2': 'base', 'e3': 'base', 'e4': 'base', 'e5': 'base'}
    state.load = {'r1': NIL, 'r2': NIL, 'UAV': NIL}
    state.storm = {'active': False}

tasks = {
    5: [['doActivities', 'UAV', [['survey', 'z6'], ['survey', 'z3'], ['survey', 'z4']]]],
    7: [['handleEmergency', 'r2', 'base']],
}

eventsEnv = {
    7: [alienSpotted, ['z2']]
}