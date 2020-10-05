__author__ = 'patras'

from domain_constants import *
import RAE1_and_RAEplan as alg

from state import state, rv
import gui
from timer import globalTimer
import GLOBALS

'''A spring door closes automatically when not held. There are two robots
to carry objects and open doors. Each robot has only one arm with which it can
either hold the door or carry the object. The goal for the main robot is to find
an object and bring it to the hallway.'''

def SD_GETDOOR(l1, l2):
    if (l1, l2) in rv.DOORLOCATIONS:
        return rv.DOORLOCATIONS[l1, l2]
    else:
        return rv.DOORLOCATIONS[l2, l1]

# Using Dijsktra's algorithm
def SD_GETPATH(l0, l1):
    visitedDistances = {l0: 0}
    locs = list(rv.LOCATIONS)
    path = {}

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
                path[l] = min_loc

    l = l1
    path2 = {}
    while l != l0:
        path2[path[l]] = l
        l = path[l]

    return path2
#****************************************************************

def fail():
    return FAILURE

def helpRobot(r1, r2):
    if state.loc[r1] == state.loc[r2]:
        gui.Simulate("%s is helping %s \n" %(r1, r2))
        return SUCCESS
    else:
        return FAILURE

def unlatch1(r, d):
    state.load.AcquireLock(r)
    state.doorStatus.AcquireLock(d)
    if state.doorStatus[d] != 'closed':
        gui.Simulate("Door %s is already open\n" %d)
        res = SUCCESS
    elif state.load[r] == NIL:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('unlatch1', start) == False):
	        pass
        res = Sense('unlatch1')
        if res == SUCCESS:
            gui.Simulate("Robot %s has opened door %s\n" %(r, d))
            state.doorStatus[d] = 'opened'
        else:
            gui.Simulate("Unlatching has failed due to an internal error\n")
    else:
        gui.Simulate("Robot %s is not free to open door %s\n" %(r, d))
        res = FAILURE
    state.load.ReleaseLock(r)
    state.doorStatus.ReleaseLock(d)
    return res

def unlatch2(r, d):
    state.load.AcquireLock(r)
    state.doorStatus.AcquireLock(d)
    if state.doorStatus[d] != 'closed': # status can be closed, opened or held
        gui.Simulate("Door %s is already open\n" %d)
        res = SUCCESS
    elif state.load[r] == NIL:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('unlatch2', start) == False):
            pass
        res = Sense('unlatch2')
        if res == SUCCESS:
            gui.Simulate("Robot %s has opened door %s\n" %(r, d))
            state.doorStatus[d] = 'opened'
        else:
            gui.Simulate("Unlatching has failed due to an internal error\n")
    else:
        gui.Simulate("Robot %s is not free to open door %s\n" %(r, d))
        res = FAILURE
    state.load.ReleaseLock(r)
    state.doorStatus.ReleaseLock(d)
    return res

def passDoor(r, d, l):
    state.doorStatus.AcquireLock(d)
    state.loc.AcquireLock(r)
    if state.doorStatus[d] == 'opened' or state.doorStatus[d] == 'held':
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('passDoor', start) == False):
	        pass
        res = Sense('passDoor', d)
        if res == SUCCESS:
            state.loc[r] = l
            gui.Simulate("Robot %s has passed the door %s\n" %(r, d))
        else:
            gui.Simulate("Robot %s is not able to pass door %s\n" %(r, d))
        state.doorType[d] = rv.DOORTYPES[d]
    else:
        gui.Simulate("Robot %s is not able to pass door %s\n" %(r, d))
        res = FAILURE
    state.loc.ReleaseLock(r)
    state.doorStatus.ReleaseLock(d)
    return res

# should always be followed by releaseDoor
def holdDoor(r, d):
    state.doorStatus.AcquireLock(d)
    state.load.AcquireLock(r)
    if state.doorStatus[d] != 'closed' and state.load[r] == NIL:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('holdDoor', start) == False):
	        pass
        gui.Simulate("Robot %s is holding the door %s\n" %(r, d))
        state.load[r] = 'H'
        state.doorStatus[d] = 'held'
        res = SUCCESS
    elif state.doorStatus[d] == 'closed':
        gui.Simulate("Door %s is closed and cannot be held by %s\n" %(d, r))
        res = FAILURE
    elif state.load[r] != NIL:
        gui.Simulate("Robot %s is not free to hold the door %s\n" %(r, d))
        res = FAILURE
    state.doorStatus.ReleaseLock(d)
    state.load.ReleaseLock(r)
    return res

def releaseDoor(r, d):
    if state.doorStatus[d] != 'held':
        return SUCCESS
    elif state.doorStatus[d] == 'held' and state.load[r] == 'H':
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('releaseDoor', start) == False):
	        pass
        gui.Simulate("Robot %s has released the the door %s\n" %(r, d))
        state.doorStatus[d] = 'closed'
        state.load[r] = NIL
    else:
        gui.Simulate("Robot %s is not holding door %s\n" %(r, d))
    return SUCCESS

def move(r, l1, l2):
    state.loc.AcquireLock(r)
    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
    elif state.loc[r] == l1:
        if (l1, l2) in rv.DOORLOCATIONS or (l2, l1) in rv.DOORLOCATIONS:
            gui.Simulate("Robot %s cannot move. There is a door between %s and %s \n" %(r, l1, l2))
            res = FAILURE
        else:
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('move', start) == False):
                pass
            res = Sense('move')
            if res == SUCCESS:
                gui.Simulate("Robot %s has moved from %d to %d\n" %(r, l1, l2))
                state.loc[r] = l2
            else:
                gui.Simulate("Move has failed due to some internal failure.\n")
    else:
        gui.Simulate("Invalid move by robot %s\n" %r)
        res = FAILURE
    state.loc.ReleaseLock(r)
    return res

def put(r, o):
    state.pos.AcquireLock(o)
    state.load.AcquireLock(r)
    state.loc.AcquireLock(r)
    if state.pos[o] == r:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('put', start) == False):
	        pass
        res = Sense('put')
        if res == SUCCESS:
            state.pos[o] = state.loc[r]
            state.load[r] = NIL
            gui.Simulate("Robot %s has put object %s at location %d\n" %(r,o,state.loc[r]))
        else:
            gui.Simulate("put has failed due to some internal failure.\n")
    else:
        gui.Simulate("Object %s is not with robot %s\n" %(o,r))
        res = FAILURE
    state.pos.ReleaseLock(o)
    state.load.ReleaseLock(r)
    state.loc.ReleaseLock(r)
    return res

def take(r, o):
    state.pos.AcquireLock(o)
    state.load.AcquireLock(r)
    state.loc.AcquireLock(r)
    if state.load[r] == NIL:
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
                gui.Simulate("take failed due to some internal error.\n")
        elif state.loc[r] != state.pos[o]:
            gui.Simulate("Robot %s is not at object %s's location\n" %(r, o))
            res = FAILURE
    else:
        gui.Simulate("Robot %s is not free to take anything\n" %r)
        res = FAILURE
    state.pos.ReleaseLock(o)
    state.load.ReleaseLock(r)
    state.loc.ReleaseLock(r)
    return res

def MoveThroughDoorway_Method3(r, d, l):
    """ For a robot passing a spring door without any load """
    if state.load[r] == NIL and (state.doorType[d] == 'spring' or state.doorType[d] == UNK):
        alg.do_task('unlatch', r, d)
        alg.do_command(holdDoor, r, d)
        alg.do_command(passDoor, r, d, l)
        alg.do_command(releaseDoor, r, d)
    else:
        alg.do_command(fail)

#def Restore(r, loc, cargo):
#    alg.do_task('moveTo', r, loc)
#    if cargo != NIL:
#        alg.do_command(take, r, cargo)

def MoveThroughDoorway_Method2(r, d, l, r2):
    """ For a robot passing a spring door with a load """
    if state.load[r] != NIL and (state.doorType[d] == 'spring' or state.doorType[d] == UNK):
        state.status.AcquireLock(r2)
        if state.status[r2] == 'free':
            state.status[r2] = 'busy'
            state.status.ReleaseLock(r2)
        else:
            state.status.ReleaseLock(r2)
            alg.do_command(fail)
    
        obj = state.load[r2]
        if obj != NIL:
            if obj != 'H':
                alg.do_command(put, r2, state.load[r2])
            else:
                alg.do_command(fail)
        alg.do_task('moveTo', r2, state.loc[r])
        alg.do_task('unlatch', r2, d)
        alg.do_command(holdDoor, r2, d)
        alg.do_command(passDoor, r, d, l)
        alg.do_command(releaseDoor, r2, d)
        state.status[r2] = 'free'
    else:
        alg.do_command(fail)
MoveThroughDoorway_Method2.parameters = "[(r2,) for r2 in rv.ROBOTS if r2 != r and state.status[r2] == 'free']"

def MoveThroughDoorway_Method4(r, d, l):
    """ For a robot passing a normal door with a load """
    if state.load[r] != NIL and (state.doorType[d] == 'ordinary' or state.doorType[d] == UNK):
        obj = state.load[r]
        if obj != 'H':
            alg.do_command(put, r, obj)
        else:
            gui.Simulate("%r is holding another door\n" %r)
            alg.do_command(fail)
        alg.do_task('unlatch', r, d)
        alg.do_command(take, r, obj)
        alg.do_command(passDoor, r, d, l)
    else:
        alg.do_command(fail)

def MoveThroughDoorway_Method1(r, d, l):
    """ For a robot passing a normal door without a load """
    if state.load[r] == NIL and (state.doorType[d] == 'ordinary' or state.doorType[d] == UNK):
        alg.do_task('unlatch', r, d)
        alg.do_command(passDoor, r, d, l)
    else:
        alg.do_command(fail)

def MoveTo_Method1(r, l):
    x = state.loc[r]
    if l in rv.LOCATIONS:
        path = SD_GETPATH(x, l)
        if path == None:
            gui.Simulate("Unsolvable problem. No path exists.\n")
            alg.do_command(fail)
        if path == {}:
            gui.Simulate("Robot %s is already at location %s \n" %(r, l))
        else:
            lTemp = x
            lNext = path[lTemp]
            while(lTemp != l):
                lNext = path[lTemp]
                if (lTemp, lNext) in rv.DOORLOCATIONS or (lNext, lTemp) in rv.DOORLOCATIONS:
                    d = SD_GETDOOR(lTemp, lNext)
                    alg.do_task('moveThroughDoorway', r, d, lNext)
                else:
                    alg.do_command(move, r, lTemp, lNext)
                if lNext != state.loc[r]:
                    alg.do_command(fail)
                else:
                    lTemp = lNext
    elif l in rv.ROBOTS: # maybe not used?
        loc = state.loc[l]
        alg.do_task('moveTo', r, loc)
    else:
        gui.Simulate("Robot %s going to invalid location.\n" %(r))
        alg.do_command(fail)

# def GetHelp_Method1(r1, r2):
#     #TODO: rewrite
#     if r == rv.ROBOTS[0]:
#         r2 = rv.ROBOTS[1]
#     else:
#         r2 = rv.ROBOTS[0]

#     for robo in rv.ROBOTS:
#         if state.load[robo] == NIL and robo != r:
#             r2 = robo

#     load_r2 = state.load[r2]
#     loc_r2 = state.loc[r2]
#     if load_r2 != NIL:
#         if load_r2 != 'H':
#             alg.do_command(put, r2, load_r2)
#         else:
#             gui.Simulate("%s is holding another door\n" %r2)
#             alg.do_command(fail)
#     alg.do_task('moveTo', r2, state.loc[r])
#     return r2, loc_r2, load_r2

def Fetch_Method1(r, o, l):
    state.status.AcquireLock(r)
    if state.status[r] == 'free':
        state.status[r] = 'busy'
        state.status.ReleaseLock(r)
    else:
        state.status.ReleaseLock(r)
        alg.do_command(fail)

    alg.do_task('moveTo', r, state.pos[o])
    alg.do_command(take, r, o)
    alg.do_task('moveTo', r, l)
    state.status[r] = 'free'
       
def Recover_Method1(r, r2): # multiple instances
    state.status.AcquireLock(r2)

    if state.status[r2] == 'busy':
        state.status.ReleaseLock(r2)
        alg.do_command(fail)
    else:
        state.status[r2] = 'busy'
        state.status.ReleaseLock(r2)
        alg.do_task('moveTo', r2, state.loc[r])
        alg.do_command(helpRobot, r2, r)
        state.status[r2] = 'free'
        gui.Simulate("Robot %s is helping %s to recover from collision\n" %(r2, r))
Recover_Method1.parameters = "[(r2,) for r2 in rv.ROBOTS if r2 != r and state.status[r2] == 'free']"

def Unlatch_Method1(r, d):
    alg.do_command(unlatch1, r, d)

def Unlatch_Method2(r, d):
    alg.do_command(unlatch2, r, d)

alg.declare_commands([ 
    holdDoor, 
    passDoor, 
    releaseDoor, 
    move, 
    put, 
    take,
    unlatch1,
    unlatch2,
    helpRobot,
    fail],)

alg.declare_task('fetch', 'r', 'o', 'l')
alg.declare_task('moveTo', 'r', 'l')
alg.declare_task('moveThroughDoorway', 'r', 'd', 'l')
alg.declare_task('unlatch', 'r', 'd')
alg.declare_task('collision', 'r')

alg.declare_methods('fetch', Fetch_Method1)
alg.declare_methods('moveTo', MoveTo_Method1)
alg.declare_methods('moveThroughDoorway',
    MoveThroughDoorway_Method1,
    MoveThroughDoorway_Method3,
    MoveThroughDoorway_Method4,
    MoveThroughDoorway_Method2) # has multiple method instances
alg.declare_methods('unlatch', Unlatch_Method1, Unlatch_Method2)

#events
alg.declare_methods('collision', Recover_Method1) # has multiple instances

def Heuristic1(args):
    return float("inf")

def Heuristic2(args):
    r = args[0]
    l1 = state.loc[r]
    l2 = args[2]
    dist = len(SD_GETPATH(l1, l2))
    if dist == 0:
        return float("inf")
    else:
        return 1/dist

def collision_Heuristic2(args):
    freeRobots = [r for r in rv.ROBOTS if state.status[r] == 'free']
    if freeRobots == []:
        return 0.001
    else:
        return 1

if GLOBALS.GetHeuristicName() == 'h1':
    alg.declare_heuristic('fetch', Heuristic1)
    alg.declare_heuristic('collision', Heuristic1)
elif GLOBALS.GetHeuristicName() == 'h2':
    alg.declare_heuristic('fetch', Heuristic2)
    alg.declare_heuristic('collision', collision_Heuristic2)

from env_springDoor import *