__author__ = 'patras'
from domain_searchAndRescue import *
from timer import DURATION
from state import state

def GetCostOfMove(r, l1, l2, dist):
    return dist

DURATION.TIME = {
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
rv.OBSTACLES = { (14, 13)}

def ResetState():
    state.loc = {'w1': (14,9), 'w2': (21,7), 'p1': (23,13), 'a1': (11,9)}
    state.hasMedicine = {'a1': 0, 'w1': 5, 'w2': 0}
    state.robotType = {'w1': 'wheeled', 'a1': 'uav', 'w2': 'wheeled'}
    state.status = {'w1': 'free', 'w2': 'free', 'a1': UNK, 'p1': UNK, (23,13): UNK}
    state.altitude = {'a1': 'high'}
    state.currentImage = {'a1': None}
    state.realStatus = {'w1': 'OK', 'p1': 'OK', 'w2': 'OK', 'a1': OK, (23, 13): 'hasDebri'}
    state.realPerson = {(23,13): 'p1'}
    state.newRobot = {1: None}
    state.weather = {(23,13): "dustStorm"}

tasks = {
    8: [['survey', 'a1', (23,13)]]
}
eventsEnv = {
}