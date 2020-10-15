__author__ = 'patras'
from domain_test import *
from timer import DURATION
from state import state

DURATION.TIME = {
    'c1': 5,
    'c2': 2,
    'c3': 10,
}

DURATION.COUNTER = {
    'c1': 5,
    'c2': 2,
    'c3': 10,
}

def ResetState():
    state.val = {'current': 1}

tasks = {
    5: [['t1', 5, 10]],
    6: [['t1', 1, 3]],
}

eventsEnv = {
}