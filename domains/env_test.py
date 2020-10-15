import numpy
from domain_constants import *
from domain_test import *
from state import state, rv
import random

commandProb = {
    'c1': [0.8, 0.2],
    'c2': [0.5, 0.5],
    'c3': [0.9, 0.1],
}

def Sense(cmd, d=None):
    p = commandProb[cmd]
    outcome = numpy.random.choice(len(p), 50, p=p)
    res = outcome[0]
    if res == 0:
        return SUCCESS
    else:
        return FAILURE