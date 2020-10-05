import numpy
from domain_constants import *
from state import state, rv
import GLOBALS

commandProb = {
    'survey': [0.95, 0.05],
    'monitor': [0.99, 0.01],
    'screen': [0.98, 0.02],
    'sample': [0.97, 0.03],
    'process': [0.99, 0.01],
    'take': [1, 0],
    'put': [1, 0],
    'charge': [0.96, 0.04],
    'move': [0.85, 0.15],
    'deposit': [0.80, 0.20],
    'transferData': [1, 0],
}

def Sense(cmd):
    p = commandProb[cmd]
    outcome = numpy.random.choice(len(p), 50, p=p)
    res = outcome[0]
    if res == 0:
        return SUCCESS
    else:
        return FAILURE

def SenseFly():
    if GLOBALS.GetPlanningMode() == True:
        p = [0.75, 0.25]
    else:
        if state.storm['active'] == True:
            p = [0.5, 0.5]
        else:
            p = [0.90, 0.10]

    outcome = numpy.random.choice(len(p), 50, p=p)
    res = outcome[0]
    if res == 0:
        return SUCCESS
    else:
        return FAILURE