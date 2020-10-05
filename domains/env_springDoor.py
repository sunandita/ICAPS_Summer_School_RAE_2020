import numpy
from domain_constants import *
from domain_springDoor import *
from state import state, rv
import random

commandProb = {
    'unlatch1': [0.8, 0.2],
    'unlatch2': [0.5, 0.5],
    'take': [1, 0],
    'put': [1, 0],
    'move': [0.95, 0.05],
}

def Sense(cmd, d=None):
    if cmd == 'passDoor':
        if GLOBALS.GetPlanningMode() == False:
            if rv.DOORTYPES[d] == 'spring':
                if state.doorStatus[d] == 'held':
                    return SUCCESS
                else:
                    return FAILURE
            else:
                if state.doorStatus[d] != 'closed':
                    return SUCCESS
                else:
                    return FAILURE
        else:
            if state.doorType[d] == UNK:
                if state.doorStatus[d] == 'held':
                    return SUCCESS
                elif state.doorStatus[d] == 'closed':
                    return FAILURE
                else:
                    return random.choice([SUCCESS, FAILURE])
            elif state.doorType[d] == 'spring':
                if state.doorStatus[d] == 'held':
                    return SUCCESS
                else:
                    return FAILURE
            else:
                if state.doorStatus[d] != 'closed':
                    return SUCCESS
                else:
                    return FAILURE

    p = commandProb[cmd]
    outcome = numpy.random.choice(len(p), 50, p=p)
    res = outcome[0]
    if res == 0:
        return SUCCESS
    else:
        return FAILURE