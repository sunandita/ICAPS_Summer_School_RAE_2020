__author__ = 'patras'

'''
A test domain to play with during Summer School 2020
'''

from domain_constants import *
import RAE1_and_UPOM as alg
import gui
from state import state, rv
from timer import globalTimer
import GLOBALS


def fail():
    return FAILURE

def c1():
    gui.Simulate("Doing c1.")
    return SUCCESS

def c2():
    gui.Simulate("Doing c2.")

alg.declare_commands([c1, c2, fail])

alg.declare_task('t1', 'a', 'b')
alg.declare_task('t2', 'c')

alg.declare_methods('t1', t1_m1, t1_m2)
alg.declare_methods('t2', t2_m1, t2_m2, t2_m3)

def Heuristic1(args):
    return float("inf")

if GLOBALS.GetHeuristicName() == 'h1' or GLOBALS.GetHeuristicName() == 'h2':
    alg.declare_heuristic('t1', Heuristic1)
    alg.declare_heuristic('t2', Heuristic1)
    
from env_test import *