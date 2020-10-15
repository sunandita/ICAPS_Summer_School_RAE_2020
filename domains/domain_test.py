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
    gui.Simulate("Doing c1.\n")
    res = Sense('c1')
    return res

def c2():
    gui.Simulate("Doing c2.\n")
    res = Sense('c1')
    return res

def c3():
    gui.Simulate("Doing c3.\n")
    res = Sense('c3')
    return res

def t1_m1(a, b):
	c = (a + b)/state.val['current']
	gui.Simulate(c)
	alg.do_command(c1)
	alg.do_command(c3)

def t1_m2(a, b):
	alg.do_command(c2)
	alg.do_command(c3)

alg.declare_commands([c1, c2, c3, fail])

alg.declare_task('t1', 'a', 'b')

alg.declare_methods('t1', t1_m1, t1_m2)

def Heuristic1(args):
    return float("inf")

if GLOBALS.GetHeuristicName() == 'h1' or GLOBALS.GetHeuristicName() == 'h2':
    alg.declare_heuristic('t1', Heuristic1)
    
from env_test import *