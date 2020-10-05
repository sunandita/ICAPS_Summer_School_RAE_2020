import numpy
from domain_IndustryPlant import rv
from domain_constants import *

commandProb = {
    'paint': [0.80, 0.20],
    #'assemble': [0.75, 0.25],
    'assemble': [1, 0.0],
    'pack': [1, 0.0],
    'wrap': [0.60, 0.40],
    'take': [1, 0],
    'put': [1, 0],
    'move': [0.99, 0.01],
}

def SenseMove(l):
    if l in rv.SLIPPERYLOCATIONS:
        p = [0.5, 0.5]
    else:
        p = [0.99, 0.01]
        
    outcome = numpy.random.choice(len(p), 50, p=p)
    res = outcome[0]
    if res == 0:
        return SUCCESS
    else:
        return FAILURE

def Sense(cmd):
    p = commandProb[cmd]
    outcome = numpy.random.choice(len(p), 50, p=p)
    res = outcome[0]
    if res == 0:
        return SUCCESS
    else:
        return FAILURE