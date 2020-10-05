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
rv.LOCATIONS = ['base', 'z1', 'z2', 'z3', 'z4']
rv.EDGES = {'base': {'z1': 20, 'z2': 50, 'z3': 20, 'z4': 50}, 'z1': {'base': 20, 'z2': 30, 'z4': 50}, 'z2': {'base': 50, 'z1': 30, 'z3': 30}, 'z3': {'base': 20, 'z2': 30, 'z4': 30}, 'z4': {'base': 50, 'z3': 30, 'z1': 50}}

def ResetState():
    state.loc = {'r1': 'base', 'r2': 'base', 'UAV': 'base'}
    state.charge = { 'UAV': 80, 'r1': 50, 'r2': 50}
    state.data = { 'UAV': 3, 'r1': 1, 'r2': 1}
    state.pos = {'c1': 'base', 'e1': 'r2', 'e2': 'base', 'e3': 'base', 'e4': 'base', 'e5': 'base'}
    state.load = {'r1': NIL, 'r2': 'e1', 'UAV': NIL}
    state.storm = {'active': False}

tasks = {
    5: [['doActivities', 'UAV', [['survey', 'z3'], ['survey', 'z1'], ['survey', 'base']]]],
}
eventsEnv = {
}