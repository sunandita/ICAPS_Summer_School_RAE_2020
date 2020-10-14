__author__ = 'patras'

import threading
import sys

sys.path.append('../shared/')
sys.path.append('../domains/')
sys.path.append('../problems/SD/auto')
sys.path.append('../problems/CR/auto')
sys.path.append('../problems/EE/auto')
sys.path.append('../problems/OF/auto')
sys.path.append('../problems/SR/auto')

import argparse
import gui
import GLOBALS
from RAE import raeMult, InitializeDomain
from RAE1_and_UPOM import verbosity
from timer import SetMode
import multiprocessing
import os

def testRAEandPlanner(domain, problem, usePlanner):
    '''
    :param domain: the code of the domain
    :param problem: the problem id
    :param usePlanner: bool value indicating whether to do planning or not before executing the tasks and events
    :return:
    '''
    domain_module = InitializeDomain(domain, problem)
    GLOBALS.SetPlanner(usePlanner)
    GLOBALS.SetPlanningMode(False) # planning mode is required to switch between acting and planning
                                   # because some code is shared between RAE, RAEplan and UPOM
    try:
        rM = threading.Thread(target=raeMult)
        rM.start()
        gui.start(domain, domain_module.rv) # graphical user interface to show action executions
        rM.join()
    except Exception as e:
        print('Failed RAE and {} {}'.format(usePlanner, e))

def testBatch(domain, problem, usePlanner):
    SetMode('Counter')
    verbosity(0)
    GLOBALS.SetShowOutputs('off')
    GLOBALS.SetDomain(domain)
    GLOBALS.SetDoIterativeDeepening(False)
    p = multiprocessing.Process(target=testRAEandPlanner, args=(domain, problem, usePlanner))
    p.start()
    p.join(GLOBALS.GetTimeLimit())
    if p.is_alive() == True:
        p.terminate()
        print("0 1 0 0 0 0 0 0 0")
    
# Specifically set parameters for the SDN domain
def InitializeSecurityDomain(v, state):
    GLOBALS.SetMaxDepth(float("inf"))
    verbosity(v)
    SetMode('Counter')
    GLOBALS.SetShowOutputs('on')
    GLOBALS.SetPlanner("UPOM")
    GLOBALS.SetDataGenerationMode(None) # for learning
    GLOBALS.Set_nRO(50) # to decide accordingly
    GLOBALS.SetTimeLimit(300) # in secs
    GLOBALS.SetDoIterativeDeepening(False)
    '''
    :param domain: the code of the domain
    :param problem: the problem id
    '''
    InitializeDomain('SDN_dev', None, state) # no concept of separate problem in SDN, so the second argument is None
    GLOBALS.SetDomain('SDN_dev')
    GLOBALS.SetUtility('resilience') # maximizing the resilience (0 or 1+1/sum(cost))
    GLOBALS.SetUseTrainedModel(None) # for learning, in case you have models
    GLOBALS.SetPlanningMode(False) # planning mode is required to switch between acting and planning
                                   # because some code is shared by both RAE and RAEplan
    try:
        rM = threading.Thread(target=raeMult)
        rM.start()
    except Exception as e:
        print('Failed to start RAE and RAEplan {}'.format(e))
    return taskQueue, cmdExecQueue, cmdStatusQueue 


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--v", help="verbosity of RAE's debugging output (0, 1 or 2)",
                           type=int, default=0, required=False)
    argparser.add_argument("--domain", help="name of the test domain (CR, SD, EE, IP, OF, SR, SDN)",
                           type=str, default='CR', required=False)
    argparser.add_argument("--problem", help="identifier for the problem eg. 'problem1', 'problem2', etc",
                           type=str, default="problem11", required=False)

    argparser.add_argument("--planner", help="Which planner to use? UPOM or None",
                           type=str, default="problem11", required=False)

    argparser.add_argument("--depth", help="Maximum Search Depth",
                           type=int, default=50, required=False)
    argparser.add_argument("--heuristic", help="Name of the heuristic function",
                           type=str, default='h2', required=False)

    argparser.add_argument("--timeLim", help="What is the time limit for running RAE? ",
                           type=int, default=300, required=False)
    # parameter for UPOM
    argparser.add_argument("--n_RO", help="Number of rollouts in UPOM?",
                           type=int, default=500, required=False)

    #what to optimize?
    argparser.add_argument("--utility", help="efficiency or successRatio?",
                           type=str, default="efficiency", required=False)

    argparser.add_argument("--doIterativeDeepening", help="Increment depth in steps of 5?",
                        type=bool, default=False, required=False)

    args = argparser.parse_args()


    assert(args.depth >= 1)
    GLOBALS.SetMaxDepth(args.depth)
    GLOBALS.SetHeuristicName(args.heuristic)

    verbosity(args.v)
    SetMode("Counter")

    GLOBALS.SetShowOutputs("on")

    GLOBALS.Set_nRO(args.n_RO)
    GLOBALS.SetDomain(args.domain)
    GLOBALS.SetTimeLimit(args.timeLim)
    GLOBALS.SetDataGenerationMode(None)
    GLOBALS.SetUseTrainedModel(None)
    GLOBALS.SetModelPath("..")
    GLOBALS.SetDoIterativeDeepening(args.doIterativeDeepening)

    GLOBALS.SetBackupUCT(False) # for SDN

    assert(args.utility == "efficiency" or args.utility == "successRatio" or args.utility == "resilience")
    GLOBALS.SetUtility(args.utility)
    testRAEandPlanner(args.domain, args.problem, args.planner)
    
