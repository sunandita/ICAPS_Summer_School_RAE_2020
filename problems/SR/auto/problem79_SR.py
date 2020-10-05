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
    state.loc = {'w1': (7,16), 'w2': (29,6), 'p1': (16,26), 'a1': (29,27)}
    state.hasMedicine = {'a1': 0, 'w1': 0, 'w2': 0}
    state.robotType = {'w1': 'wheeled', 'a1': 'uav', 'w2': 'wheeled'}
    state.status = {'w1': 'free', 'w2': 'free', 'a1': UNK, 'p1': UNK, (16,26): UNK}
    state.altitude = {'a1': 'high'}
    state.currentImage = {'a1': None}
    state.realStatus = {'w1': 'OK', 'p1': 'OK', 'w2': 'OK', 'a1': OK, (16, 26): 'hasDebri'}
    state.realPerson = {(16,26): 'p1'}
    state.newRobot = {1: None}
    state.weather = {(16,26): "dustStorm"}

tasks = {
    4: [['survey', 'a1', (16,26)]]
}
eventsEnv = {
}