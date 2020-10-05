import GLOBALS
import numpy
from state import state
from domain_searchAndRescue import rv
from domain_constants import *

commandProb = {
    'giveSupportToPerson': [0.9, 0.1],
    'clearLocation': [0.8, 0.2],
    'inspectPerson': [0.8, 0.2],
    'moveEuclidean': [0.95, 0.05],
    'moveCurved': [0.95, 0.05],
    'moveManhattan': [0.95, 0.05],
    'fly': [0.9, 0.1],
    'inspectLocation': [0.98, 0.02],
    'changeAltitude': [0.8, 0.2]
}

def Sense(cmd, *cmdArgs):
    if cmd == 'perceive':
        if globals.GetPlanningMode() == True:
            return SenseObjects()
        else:
            return SUCCESS
    elif cmd == 'wait':
        if globals.GetPlanningMode() == True:
            for r in rv.ROBOTS:
                state.emergencyHandling[r] = False
    elif cmd == 'captureImage':
        return SenseImage(*cmdArgs)
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

def SenseImage(r, camera, l):
    img = {'loc': None, 'person': None}
    visibility = False
    if state.weather[l] == 'rainy':
        if camera == 'bottomCamera' and state.altitude[r] == 'low':
            visibility = True
    elif state.weather[l] == 'foggy':
        if camera == 'frontCamera' and state.altitude[r] == 'low':
            visibility = True
    elif state.weather[l] == 'dustStorm':
        if state.altitude[r] == 'low':
            visibility = True
    elif state.weather[l] == 'clear':
        visibility = True
    else:
        print("Invalid weather conditions. Please check problem file.\n")

    if visibility == True:
        img['loc'] = l
        img['person'] = state.realPerson[l]

    return img
