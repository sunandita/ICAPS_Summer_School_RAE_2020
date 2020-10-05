import GLOBALS
import numpy
from state import state
from domain_chargeableRobot import rv
from domain_constants import *

commandProb = {
    'take': [0.9, 0.1],
    'put': [0.99, 0.01],
    'charge': [0.90, 0.10],
    'moveToEmergency': [0.99, 0.01],
    'move': [0.95, 0.05],
    'addressEmergency': [0.98, 0.02],
}

def Sense(cmd):
    if cmd == 'perceive':
        if GLOBALS.GetPlanningMode() == True:
            return SenseObjects()
        else:
            return SUCCESS
    elif cmd == 'wait':
        if GLOBALS.GetPlanningMode() == True:
            for r in rv.ROBOTS:
                state.emergencyHandling[r] = False
    else:
        p = commandProb[cmd]
        outcome = numpy.random.choice(len(p), 50, p=p)
        res = outcome[0]
        if res == 0:
            return SUCCESS
        else:
            return FAILURE

def SenseObjects():
    total = 0
    for loc in state.containers:
        state.containers[loc] = []
        if state.view[loc] == False:
            total += 1

    for o in rv.OBJECTS:
        prob = {}
        if state.pos[o] == UNK:
            for l in state.view:
                if state.view[l] == False:
                    prob[l] = 1/total
            p = list(prob.values())
            locs = list(prob.keys())
            locIndex = numpy.random.choice(len(p), 50, p=p)
            state.containers[locs[locIndex[0]]].append(o)