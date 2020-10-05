__author__ = 'patras'
from domain_searchAndRescue import *
from timer import DURATION
from state import state

def GetCostOfMove(r, l1, l2, dist):
    return dist

DURATION.COUNTER = {
    'giveSupportToPerson': 15,
    'clearLocation': 5,
    'inspectPerson': 20,
    'moveEuclidean': GetCostOfMove,
    'moveCurved': GetCostOfMove,
    'moveManhattan': GetCostOfMove,
    'fly': 15,
    'inspectLocation': 5,
    'transfer': 2,
    'replenishSupplies': 4,
    'captureImage': 2,
    'changeAltitude': 3,
    'deadEnd': 1,
}

DURATION.COUNTER = {
    'giveSupportToPerson': 15,
    'clearLocation': 5,
    'inspectPerson': 20,
    'moveEuclidean': GetCostOfMove,
    'moveCurved': GetCostOfMove,
    'moveManhattan': GetCostOfMove,
    'fly': 15,
    'inspectLocation': 5,
    'transfer': 2,
    'replenishSupplies': 4,
    'captureImage': 2,
    'changeAltitude': 3,
    'deadEnd': 1,
}

rv.WHEELEDROBOTS = ['w1', 'w2']
rv.DRONES = ['a1']
rv.OBSTACLES = { (100, 100)}

def ResetState():
    state.loc = {'w1': (30,24), 'w2': (14,27), 'p1': (15,14), 'a1': (11,26)}
    state.hasMedicine = {'a1': 0, 'w1': 5, 'w2': 0}
    state.robotType = {'w1': 'wheeled', 'a1': 'uav', 'w2': 'wheeled'}
    state.status = {'w1': 'free', 'w2': 'free', 'a1': UNK, 'p1': UNK, (15,14): UNK}
    state.altitude = {'a1': 'high'}
    state.currentImage = {'a1': None}
    state.realStatus = {'w1': 'OK', 'p1': 'injured', 'w2': 'OK', 'a1': OK, (15, 14): 'clear'}
    state.realPerson = {(15,14): 'p1'}
    state.newRobot = {1: None}
    state.weather = {(15,14): "foggy"}

tasks = {
    7: [['survey', 'a1', (15,14)]]
}
eventsEnv = {
}