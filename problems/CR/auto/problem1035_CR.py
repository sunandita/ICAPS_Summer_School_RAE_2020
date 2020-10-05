# uncompyle6 version 3.3.1
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
# Embedded file name: ../../shared/problems/CR/problem1035_CR.py
# Compiled at: 2019-03-12 17:52:21
# Size of source mod 2**32: 1111 bytes
__author__ = 'patras'
from domain_chargeableRobot import *
from timer import DURATION
from state import state
DURATION.TIME = {'put':2, 
 'take':2, 
 'perceive':2, 
 'charge':2, 
 'move':2, 
 'moveToEmergency':2, 
 'moveCharger':2, 
 'addressEmergency':2, 
 'wait':2}
DURATION.COUNTER = {'put':2, 
 'take':2, 
 'perceive':2, 
 'charge':2, 
 'move':2, 
 'moveToEmergency':2, 
 'moveCharger':2, 
 'addressEmergency':2, 
 'wait':2}
rv.LOCATIONS = [
 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rv.EDGES = {1:[2],  2:[1, 3],  3:[2, 4],  4:[5, 3, 6, 7],  5:[4, 9],  6:[4, 10],  7:[4, 8],  8:[7],  9:[5],  10:[6]}
rv.OBJECTS = ['o1']
rv.ROBOTS = [
 'r1']

def ResetState():
    state.loc = {'r1': 1}
    state.charge = {'r1': 1}
    state.load = {'r1': NIL}
    state.pos = {'c1':1,  'o1':9}
    state.containers = {1:[],  2:[],  3:[],  4:[],  5:[],  6:[],  7:[],  8:[],  9:['o1'],  10:[]}
    state.emergencyHandling = {'r1':False,  'r2':False}
    state.view = {}
    for l in rv.LOCATIONS:
        state.view[l] = False


tasks = {6: [['fetch', 'r1', 'o1']]}
eventsEnv = {}
# okay decompiling __pycache__/problem1035_CR.cpython-36.pyc
