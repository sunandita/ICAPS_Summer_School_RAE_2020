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
rv.LOCATIONS = ['base', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7']
rv.EDGES = {'base': {'z1': 15, 'z4': 15, 'z5': 35, 'z6': 35, 'z7': 35}, 'z1': {'base': 15, 'z2': 30}, 'z2': {'z1': 30, 'z3': 30}, 'z3': {'z2': 30, 'z4': 30}, 'z4': {'z3': 30, 'base': 15}, 'z5': {'base': 35}, 'z6': {'base': 35}, 'z7': {'base': 35}}

def ResetState():
    state.loc = {'r1': 'base', 'r2': 'base', 'UAV': 'base'}
    state.charge = { 'UAV': 80, 'r1': 80, 'r2': 50}
    state.data = { 'UAV': 1, 'r1': 1, 'r2': 3}
    state.pos = {'c1': 'base', 'e1': 'base', 'e2': 'base', 'e3': 'base', 'e4': 'base', 'e5': 'base'}
    state.load = {'r1': NIL, 'r2': NIL, 'UAV': NIL}
    state.storm = {'active': True}

tasks = {
    6: [['doActivities', 'UAV', [['survey', 'z6'], ['survey', 'z2']]]],
    8: [['doActivities', 'r1', [['screen', 'z5'], ['screen', 'z2'], ['process', 'z4']]]],
}
eventsEnv = {
}