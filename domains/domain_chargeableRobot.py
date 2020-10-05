__author__ = 'patras'

'''A robot is searching for an object in the environment consisting of a few locations.
It has a battery that needs to be recharged after some moves.
A move consumes 1/4 of the battery capacity.'''

from domain_constants import *
#import importlib
#loader = importlib.find_loader('RAE1_and_RAEplan')
#if loader is not None:
import RAE1_and_RAEplan as alg
import gui
from state import state, rv
from timer import globalTimer
import GLOBALS

# Using Dijsktra's algorithm
def CR_GETDISTANCE(l0, l1):
    visitedDistances = {l0: 0}
    locs = list(rv.LOCATIONS)

    while locs:
        min_loc = None
        for loc in locs:
            if loc in visitedDistances:
                if min_loc is None:
                    min_loc = loc
                elif visitedDistances[loc] < visitedDistances[min_loc]:
                    min_loc = loc

        if min_loc is None:
            break

        locs.remove(min_loc)
        current_dist = visitedDistances[min_loc]

        for l in rv.EDGES[min_loc]:
            dist = current_dist + 1
            if l not in visitedDistances or dist < visitedDistances[l]:
                visitedDistances[l] = dist

    return visitedDistances[l1]

def fail():
    return FAILURE

def take(r, o):
    state.load.AcquireLock(r)
    if state.load[r] == NIL:
        state.pos.AcquireLock(o)
        if state.loc[r] == state.pos[o]:
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('take', start) == False):
                pass
            res = Sense('take')
            if res == SUCCESS:
                gui.Simulate("Robot %s has picked up object %s\n" %(r, o))
                state.pos[o] = r
                state.load[r] = o
            else:
                gui.Simulate("Non-deterministic event has made the take command fail\n")
        else:
            gui.Simulate("Robot %s is not at object %s's location\n" %(r, o))
            res = FAILURE
        state.pos.ReleaseLock(o)
    else:
        gui.Simulate("Robot %s is not free to take anything\n" %r)
        res = FAILURE
    state.load.ReleaseLock(r)
    return res

def put(r, o):
    state.pos.AcquireLock(o)
    if state.pos[o] == r:
        start = globalTimer.GetTime()
        state.loc.AcquireLock(r)
        state.load.AcquireLock(r)
        while(globalTimer.IsCommandExecutionOver('put', start) == False):
            pass
        res = Sense('put')
        if res == SUCCESS:    
            gui.Simulate("Robot %s has put object %s at location %d\n" %(r,o,state.loc[r]))
            state.pos[o] = state.loc[r]
            state.load[r] = NIL
        else:
            gui.Simulate("Robot %s has failed to put %s because of some internal error")
        state.loc.ReleaseLock(r)
        state.load.ReleaseLock(r)
    else:
        gui.Simulate("Object %s is not with robot %s\n" %(o,r))
        res = FAILURE
    state.pos.ReleaseLock(o)
    return res

def charge(r, c):
    state.loc.AcquireLock(r)
    state.pos.AcquireLock(c)
    if state.loc[r] == state.pos[c] or state.pos[c] == r:
        state.charge.AcquireLock(r)
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('charge', start) == False):
            pass
        res = Sense('charge')
        if res == SUCCESS:
            state.charge[r] = 4
            gui.Simulate("Robot %s is fully charged\n" %r)
        else:
            gui.Simulate("Charging of robot %s failed due to some internal error.\n" %r)
        state.charge.ReleaseLock(r)
    else:
        gui.Simulate("Robot %s is not in the charger's location or it doesn't have the charger with it\n" %r)
        res = FAILURE
    state.loc.ReleaseLock(r)
    state.pos.ReleaseLock(c)
    return res

def moveToEmergency(r, l1, l2, dist):
    state.loc.AcquireLock(r)
    state.charge.AcquireLock(r)
    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
    elif state.loc[r] == l1 and state.charge[r] >= dist:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('move', start) == False):
           pass
        res = Sense('moveToEmergency')
        if res == SUCCESS:
            gui.Simulate("Robot %s has moved from %d to %d\n" %(r, l1, l2))
            state.loc[r] = l2
            state.charge[r] = state.charge[r] - dist
        else:
            gui.Simulate("Moving failed due to some internal error\n")
    elif state.loc[r] != l1 and state.charge[r] >= dist:
        gui.Simulate("Robot %s is not in location %d\n" %(r, l1))
        res = FAILURE
    elif state.loc[r] == l1 and state.charge[r] < dist:
        gui.Simulate("Robot %s does not have enough charge to move :(\n" %r)
        state.charge[r] = 0 # should we do this?
        res = FAILURE
    else:
        gui.Simulate("Robot %s is not at location %s and it doesn't have enough charge!\n" %(r, l1))
        res = FAILURE
    state.loc.ReleaseLock(r)
    state.charge.ReleaseLock(r)
    if res == FAILURE:
        state.emergencyHandling.AcquireLock(r)
        state.emergencyHandling[r] = False
        state.emergencyHandling.ReleaseLock(r)
    return res

def perceive(l):
    state.view.AcquireLock(l)
    if state.view[l] == False:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('perceive', start) == False):
            pass
        Sense('perceive')
        for c in state.containers[l]:
            state.pos.AcquireLock(c)
            state.pos[c] = l
            state.pos.ReleaseLock(c)
        state.view[l] = True
        gui.Simulate("Perceived location %d\n" %l)
    else:
        gui.Simulate("Already perceived\n")
    state.view.ReleaseLock(l)
    return SUCCESS

def move(r, l1, l2, dist):
    state.emergencyHandling.AcquireLock(r)
    if state.emergencyHandling[r] == False:
        state.loc.AcquireLock(r)
        state.charge.AcquireLock(r)
        if l1 == l2:
            gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
            res = SUCCESS
        elif state.loc[r] == l1 and (state.charge[r] >= dist or state.load[r] == 'c1'):
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('move', start) == False):
               pass
            res = Sense('move')
            if res == SUCCESS:
                gui.Simulate("Robot %s has moved from %d to %d\n" %(r, l1, l2))
                state.loc[r] = l2
                if state.load[r] != 'c1':
                    state.charge[r] = state.charge[r] - dist
            else:
                gui.Simulate("Robot %s failed to move due to some internal failure\n" %r)
        elif state.loc[r] != l1 and state.charge[r] >= dist:
            gui.Simulate("Robot %s is not in location %d\n" %(r, l1))
            res = FAILURE
        elif state.loc[r] == l1 and state.charge[r] < dist:
            gui.Simulate("Robot %s does not have enough charge to move :(\n" %r)
            state.charge[r] = 0 # should we do this?
            res = FAILURE
        else:
            gui.Simulate("Robot %s is not at location %s and it doesn't have enough charge!\n" %(r, l1))
            res = FAILURE
        state.loc.ReleaseLock(r)
        state.charge.ReleaseLock(r)
    else:
        gui.Simulate("Robot is addressing emergency so it cannot move.\n")
        res = FAILURE
    state.emergencyHandling.ReleaseLock(r)
    return res

def addressEmergency(r, l, i):
    state.loc.AcquireLock(r)
    state.emergencyHandling.AcquireLock(r)
    if state.loc[r] == l:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('addressEmergency', start) == False):
            pass
        res = Sense('addressEmergency')
        if res == SUCCESS:
            gui.Simulate("Robot %s has addressed emergency %d\n" %(r, i))
        else:
            gui.Simulate("Robot %s has failed to address emergency due to some internal error \n" %r)
    else:
        gui.Simulate("Robot %s has failed to address emergency %d\n" %(r, i))
        res = FAILURE
    state.emergencyHandling[r] = False
    state.loc.ReleaseLock(r)
    state.emergencyHandling.ReleaseLock(r)
    return res

def wait(r):
    while(state.emergencyHandling[r] == True):
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('wait', start) == False):
            pass
        gui.Simulate("Robot %s is waiting for emergency to be over\n" %r)
        Sense('wait')
    return SUCCESS

def Recharge_Method3(r, c):
    """ Robot r charges and carries the charger with it """
    if state.loc[r] != state.pos[c] and state.pos[c] != r:
        if state.pos[c] in rv.LOCATIONS:
            alg.do_task('moveTo', r, state.pos[c])
        else:
            robot = state.pos[c]
            alg.do_command(put, robot, c)
            alg.do_task('moveTo', r, state.pos[c])
    alg.do_command(charge, r, c)
    alg.do_command(take, r, c)

def Recharge_Method2(r, c):
    """ Robot r charges and does not carry the charger with it """
    if state.loc[r] != state.pos[c] and state.pos[c] != r:
        if state.pos[c] in rv.LOCATIONS:
            alg.do_task('moveTo', r, state.pos[c])
        else:
            robot = state.pos[c]
            alg.do_command(put, robot, c)
            alg.do_task('moveTo', r, state.pos[c])
    alg.do_command(charge, r, c)

def Recharge_Method1(r, c):
    """ When the charger is with another robot and that robot takes the charger back """ 
    robot = NIL
    if state.loc[r] != state.pos[c] and state.pos[c] != r:
        if state.pos[c] in rv.LOCATIONS:
            alg.do_task('moveTo', r, state.pos[c])
        else:
            robot = state.pos[c]
            alg.do_command(put, robot, c)
            alg.do_task('moveTo', r, state.pos[c])
    alg.do_command(charge, r, c)
    if robot != NIL:
        alg.do_command(take, robot, c)

def Search_Method1(r, o):
    if state.pos[o] == UNK:
        toBePerceived = NIL
        for l in rv.LOCATIONS:
            if state.view[l] == False:
                toBePerceived = l
                break

        if toBePerceived != NIL:
            alg.do_task('moveTo', r, toBePerceived)
            alg.do_command(perceive, toBePerceived)
            if state.pos[o] == toBePerceived:
                if state.load[r] != NIL:
                    alg.do_command(put, r, state.load[r])
                alg.do_command(take, r, o)
            else:
                alg.do_task('search', r, o)
        else:
            gui.Simulate("Failed to search %s" %o)
            alg.do_command(fail)
    else:
        gui.Simulate("Position of %s is already known\n" %o)

def Search_Method2(r, o):
    if state.pos[o] == UNK:
        toBePerceived = NIL
        for l in rv.LOCATIONS:
            if state.view[l] == False:
                toBePerceived = l
                break

        if toBePerceived != NIL:
            alg.do_task('recharge', r, 'c1') # is this allowed?
            alg.do_task('moveTo', r, toBePerceived)
            alg.do_command(perceive, toBePerceived)
            if state.pos[o] == toBePerceived:
                if state.load[r] != NIL:
                    alg.do_command(put, r, state.load[r])
                alg.do_command(take, r, o)
            else:
                alg.do_task('search', r, o)
        else:
            gui.Simulate("Failed to search %s" %o)
            alg.do_command(fail)
    else:
        gui.Simulate("Position of %s is already known\n" %o)

def Fetch_Method1(r, o):
    pos_o = state.pos[o]
    if pos_o == UNK:
        alg.do_task('search', r, o)
    else:
        if state.loc[r] != pos_o:
            alg.do_task('moveTo', r, pos_o)
        if state.load[r] != NIL:
            alg.do_command(put, r, state.load[r])
        alg.do_command(take, r, o)

def Fetch_Method2(r, o):
    pos_o = state.pos[o]
    if pos_o == UNK:
        alg.do_task('search', r, o)
    else:
        if state.loc[r] != pos_o:
            alg.do_task('recharge', r, 'c1')
            alg.do_task('moveTo', r, pos_o)
        if state.load[r] != NIL:
            alg.do_command(put, r, state.load[r])
        alg.do_command(take, r, o)

def Emergency_Method1(r, l, i):
    if state.emergencyHandling[r] == False:
        state.emergencyHandling[r] = True
        load_r = state.load[r]
        if load_r != NIL:
            alg.do_command(put, r, load_r)
        l1 = state.loc[r]
        dist = CR_GETDISTANCE(l1, l)
        alg.do_command(moveToEmergency, r, l1, l, dist)
        alg.do_command(addressEmergency, r, l, i)
    else:
        gui.Simulate("%r is already busy handling another emergency\n" %r)
        alg.do_command(fail)

def NonEmergencyMove_Method1(r, l1, l2, dist):
    if state.emergencyHandling[r] == False:
        alg.do_command(move, r, l1, l2, dist)
    else:
        alg.do_command(wait, r)
        alg.do_command(move, r, l1, l2, dist)

def MoveTo_Method1(r, l):
    x = state.loc[r]
    dist = CR_GETDISTANCE(x, l)
    if state.charge[r] >= dist or state.load[r] == 'c1':
        alg.do_task('nonEmergencyMove', r, x, l, dist)
    else:
        state.charge[r] = 0
        gui.Simulate("Robot %s does not have enough charge to move from %d to %d\n" %(r, x, l))
        alg.do_command(fail)

alg.declare_commands([put, take, perceive, charge, move, moveToEmergency, addressEmergency, wait, fail])

alg.declare_task('search', 'r', 'o')
alg.declare_task('fetch', 'r', 'o')
alg.declare_task('recharge', 'r', 'c')
alg.declare_task('moveTo', 'r', 'l')
alg.declare_task('emergency', 'r', 'l', 'i')
alg.declare_task('nonEmergencyMove', 'r', 'l1', 'l2', 'dist')

alg.declare_methods('search', Search_Method1, Search_Method2)
alg.declare_methods('fetch', Fetch_Method1, Fetch_Method2)
alg.declare_methods('recharge', Recharge_Method1, Recharge_Method2, Recharge_Method3)
alg.declare_methods('moveTo', MoveTo_Method1)
alg.declare_methods('emergency', Emergency_Method1)
alg.declare_methods('nonEmergencyMove', NonEmergencyMove_Method1)

def Heuristic1(args):
    return float("inf")

def Heuristic2(args):
    robot = args[0]
    return 5 * state.charge[robot]

if GLOBALS.GetHeuristicName() == 'h1':
    alg.declare_heuristic('search', Heuristic1)
    alg.declare_heuristic('fetch', Heuristic1)
elif GLOBALS.GetHeuristicName() == 'h2':
    alg.declare_heuristic('search', Heuristic2)
    alg.declare_heuristic('fetch', Heuristic2)
    
from env_chargeableRobot import *