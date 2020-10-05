__author__ = 'patras'

''' Search and Rescue domain:
    There are some natural disasters happening in an area.
    Robots with the help of human experts do search and rescue operations in this area. 
'''

from domain_constants import *
import importlib
#loader = importlib.find_loader('RAE1_and_RAEplan')
#if loader is not None:
import RAE1_and_RAEplan as alg
#else:
#    import ape1_and_apeplan as alg
import gui
from state import state, rv
from timer import globalTimer
import math
import GLOBALS

def fail():
    return FAILURE

def deadEnd(p):
    state.status[p] = 'dead'
    state.realStatus[p] = 'dead'
    return FAILURE

def moveEuclidean(r, l1, l2, dist):
    (x1, y1) = l1
    (x2, y2) = l2
    xlow = min(x1, x2)
    xhigh = max(x1, x2)
    ylow = min(y1, y2)
    yhigh = max(y1, y2)
    for o in rv.OBSTACLES:    
        (ox, oy) = o
        if ox >= xlow and ox <= xhigh and oy >= ylow and oy <= yhigh:
            if ox == x1 or x2 == x1:
                gui.Simulate("%s cannot move in Euclidean path because of obstacle\n" %r)
                return FAILURE
            elif abs((oy - y1)/(ox - x1) - (y2 - y1)/(x2 - x1)) <= 0.0001:
                gui.Simulate("%s cannot move in Euclidean path because of obstacle\n" %r)
                return FAILURE

    state.loc.AcquireLock(r)
    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
    elif state.loc[r] == l1:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('moveEuclidean', start, r, l1, l2, dist) == False):
           pass
        res = Sense('moveEuclidean')
        if res == SUCCESS:
            gui.Simulate("Robot %s has moved from %s to %s\n" %(r, str(l1), str(l2)))
            state.loc[r] = l2
        else:
            gui.Simulate("Robot %s failed to move due to some internal failure.\n" %r)
    else:
        gui.Simulate("Robot %s is not in location %d.\n" %(r, l1))
        res = FAILURE
    state.loc.ReleaseLock(r)
    return res

def moveCurved(r, l1, l2, dist):
    (x1, y1) = l1
    (x2, y2) = l2
    centrex = (x1 + x2)/2
    centrey = (y1 + y2)/2
    for o in rv.OBSTACLES:
        (ox, oy) = o
        r2 = (x2 - centrex)*(x2 - centrex) + (y2 - centrey)*(y2 - centrey)
        ro = (ox - centrex)*(ox - centrex) + (oy - centrey)*(oy - centrey)  
        if abs(r2 - ro) <= 0.0001:
            gui.Simulate("%s cannot move in curved path because of obstacle\n" %r)
            return FAILURE
    
    state.loc.AcquireLock(r)
    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
    elif state.loc[r] == l1:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('moveCurved', start, r, l1, l2, dist) == False):
           pass
        res = Sense('moveCurved')
        if res == SUCCESS:
            gui.Simulate("Robot %s has moved from %s to %s\n" %(r, str(l1), str(l2)))
            state.loc[r] = l2
        else:
            gui.Simulate("Robot %s failed to move due to some internal failure.\n" %r)
    else:
        gui.Simulate("Robot %s is not in location %d.\n" %(r, l1))
        res = FAILURE
    state.loc.ReleaseLock(r)
    return res

def moveManhattan(r, l1, l2, dist):
    (x1, y1) = l1
    (x2, y2) = l2
    xlow = min(x1, x2)
    xhigh = max(x1, x2)
    ylow = min(y1, y2)
    yhigh = max(y1, y2)
    for o in rv.OBSTACLES:
        (ox, oy) = o
        if abs(oy - y1) <= 0.0001 and ox >= xlow and ox <= xhigh:
            gui.Simulate("%s cannot move in Manhattan path because of obstacle\n" %r)
            return FAILURE

        if abs(ox - x2) <= 0.0001 and oy >= ylow and oy <= yhigh:
            gui.Simulate("%s cannot move in Manhattan path because of obstacle\n" %r)
            return FAILURE

    state.loc.AcquireLock(r)
    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
    elif state.loc[r] == l1:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('moveManhattan', start, r, l1, l2, dist) == False):
           pass
        res = Sense('moveManhattan')
        if res == SUCCESS:
            gui.Simulate("Robot %s has moved from %s to %s\n" %(r, str(l1), str(l2)))
            state.loc[r] = l2
        else:
            gui.Simulate("Robot %s failed to move due to some internal failure.\n" %r)
    else:
        gui.Simulate("Robot %s is not in location %d.\n" %(r, l1))
        res = FAILURE
    state.loc.ReleaseLock(r)
    return res

def fly(r, l1, l2):
    state.loc.AcquireLock(r)
    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
    elif state.loc[r] == l1:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('fly', start) == False):
           pass
        res = Sense('fly')
        if res == SUCCESS:
            gui.Simulate("Robot %s has flied from %s to %s\n" %(r, str(l1), str(l2)))
            state.loc[r] = l2
        else:
            gui.Simulate("Robot %s failed to fly due to some internal failure.\n" %r)
    else:
        gui.Simulate("Robot %s is not in location %d.\n" %(r, l1))
        res = FAILURE
    state.loc.ReleaseLock(r)
    return res

def inspectPerson(r, p):
    gui.Simulate("Robot %s is inspecting person %s \n" %(r, p))
    state.status[p] = state.realStatus[p]
    return SUCCESS

def giveSupportToPerson(r, p):
    if state.status[p] != 'dead':
        gui.Simulate("Robot %s has saved person %s \n" %(r, p))
        state.status[p] = 'OK'
        state.realStatus[p] = 'OK'
        res = SUCCESS
    else:
        gui.Simulate("Person %s is already dead \n" %(p))
        res = FAILURE
    return res

def inspectLocation(r, l):
    gui.Simulate("Robot %s is inspecting location %s \n" %(r, str(l)))
    state.status[l] = state.realStatus[l]
    return SUCCESS

def clearLocation(r, l):
    gui.Simulate("Robot %s has cleared location %s \n" %(r, str(l)))
    state.status[l] = 'clear'
    state.realStatus[l] = 'clear'
    return SUCCESS

def replenishSupplies(r):
    state.hasMedicine.AcquireLock(r)
    if state.loc[r] == (1,1):
        state.hasMedicine[r] = 5
        gui.Simulate("Robot %s has replenished supplies at the base.\n" %r)
        res = SUCCESS
    else:
        gui.Simulate("Robot %s is not at the base.\n" %r)
        res = FAILURE

    state.hasMedicine.ReleaseLock(r)
    return res

def transfer(r1, r2):
    state.hasMedicine.AcquireLock(r1)
    state.hasMedicine.AcquireLock(r2)
    if state.loc[r1] == state.loc[r2]:
        if state.hasMedicine[r1] > 0:
            state.hasMedicine[r2] += 1
            state.hasMedicine[r1] -= 1
            gui.Simulate("Robot %s has transferred medicine to %s.\n" %(r1, r2))
            res = SUCCESS
        else:
            gui.Simulate("Robot %s does not have medicines.\n" %r1)
            res = FAILURE
    else:
        gui.Simulate("Robots %s and %s are in different locations.\n" %(r1, r2))
        res = FAILURE
    state.hasMedicine.ReleaseLock(r2)
    state.hasMedicine.ReleaseLock(r1)
    return res

def captureImage(r, camera, l):
    img = Sense('captureImage', r, camera, l)

    state.currentImage.AcquireLock(r)
    state.currentImage[r] = img
    gui.Simulate("UAV %s has captured image in location %s using %s\n" %(r, l, camera))
    state.currentImage.ReleaseLock(r)
    return SUCCESS

def changeAltitude(r, newAltitude):
    state.altitude.AcquireLock(r)
    if state.altitude[r] != newAltitude:
        res = Sense('changeAltitude')
        if res == SUCCESS:
            state.altitude[r] = newAltitude
            gui.Simulate("UAV %s has changed altitude to %s\n" %(r, newAltitude))
        else:
            gui.Simulate("UAV %s was not able to change altitude to %s\n" %(r, newAltitude))
    else:
        res = SUCCESS
        gui.Simulate("UAV %s is already in %s altitude.\n" %(r, newAltitude))
    state.altitude.ReleaseLock(r)
    return res

def SR_GETDISTANCE_Euclidean(l0, l1):
    (x0, y0) = l0
    (x1, y1) = l1
    return math.sqrt((x1 - x0)*(x1 - x0) + (y1 - y0)*(y1-y0))

def MoveTo_Method1(r, l): # takes the straight path
    x = state.loc[r]
    if x == l:
        gui.Simulate("Robot %s is already in location %s\n." %(r, l))
    elif state.robotType[r] == 'wheeled':
        dist = SR_GETDISTANCE_Euclidean(x, l)
        gui.Simulate("Euclidean distance = %d " %dist)
        alg.do_command(moveEuclidean, r, x, l, dist)
    else:
        alg.do_command(fail)

def SR_GETDISTANCE_Manhattan(l0, l1):
    (x1, y1) = l0
    (x2, y2) = l1
    return abs(x2 - x1) + abs(y2 - y1)

def MoveTo_Method2(r, l): # takes a Manhattan path
    x = state.loc[r]
    if x == l:
        gui.Simulate("Robot %s is already in location %s\n." %(r, l))
    elif state.robotType[r] == 'wheeled':
        dist = SR_GETDISTANCE_Manhattan(x, l)
        gui.Simulate("Manhattan distance = %d " %dist)
        alg.do_command(moveManhattan, r, x, l, dist) 
    else:
        alg.do_command(fail)

def SR_GETDISTANCE_Curved(l0, l1):
    diameter = SR_GETDISTANCE_Euclidean(l0, l1)
    return math.pi * diameter / 2

def MoveTo_Method3(r, l): # takes a curved path
    x = state.loc[r]
    if x == l:
        gui.Simulate("Robot %s is already in location %s\n." %(r, l))
    elif state.robotType[r] == 'wheeled':
        dist = SR_GETDISTANCE_Curved(x, l)
        gui.Simulate("Curved distance = %d " %dist)
        alg.do_command(moveCurved, r, x, l, dist) 
    else:
        alg.do_command(fail)

def MoveTo_Method4(r, l):
    x = state.loc[r]
    if x == l:
        gui.Simulate("Robot %s is already in location %s\n." %(r, l))
    elif state.robotType[r] == 'uav':
        alg.do_command(fly, r, x, l)
    else:
        alg.do_command(fail)

def Rescue_Method1(r, p):
    if state.robotType[r] != 'uav':
        if state.hasMedicine[r] == 0:
            alg.do_task('getSupplies', r)
        alg.do_task('helpPerson', r, p)
    else:
        alg.do_command(fail)

def Rescue_Method2(r, p):
    if state.robotType[r] == 'uav':
        alg.do_task('getRobot')
    r2 = state.newRobot[1]
    if r2 != None:
        if state.hasMedicine[r2] == 0:
            alg.do_task('getSupplies', r2)
        alg.do_task('helpPerson', r2, p)
        state.status[r2] = 'free'
    else:
        gui.Simulate("No robot is free to help person %s\n" %p)
        alg.do_command(fail)

def HelpPerson_Method1(r, p):
    # help an injured person
    alg.do_task('moveTo', r, state.loc[p])
    alg.do_command(inspectPerson, r, p)
    if state.status[p] == 'injured':
        alg.do_command(giveSupportToPerson, r, p)
    else:
        alg.do_command(fail)

def HelpPerson_Method2(r, p):
    # help a person trapped inside some debri but not injured
    alg.do_task('moveTo', r, state.loc[p])
    alg.do_command(inspectLocation, r, state.loc[r])
    if state.status[state.loc[r]] == 'hasDebri':
        alg.do_command(clearLocation, r, state.loc[r]) 
    else:
        CheckReal(state.loc[p])
        alg.do_command(fail)
        
def GetSupplies_Method1(r):
    # get supplies from nearby robots
    r2 = None
    nearestDist = float("inf")
    for r1 in rv.WHEELEDROBOTS:
        if state.hasMedicine[r1] > 0:
            dist = SR_GETDISTANCE_Euclidean(state.loc[r], state.loc[r1])
            if dist < nearestDist:
                nearestDist = dist
                r2 = r1
    if r2 != None:
        alg.do_task('moveTo', r, state.loc[r2])
        alg.do_command(transfer, r2, r)

    else:
        alg.do_command(fail)

def GetSupplies_Method2(r):
    # get supplies from the base
    alg.do_task('moveTo', r, (1,1))
    alg.do_command(replenishSupplies, r)

def CheckReal(l):
    p = state.realPerson[l]
    if p != None:
        if state.realStatus[p] == 'injured' or state.realStatus[p] == 'dead' or state.realStatus[l] == 'hasDebri':
            gui.Simulate("Person in location %s failed to be saved.\n" %str(l))
            alg.do_command(deadEnd, p)
            alg.do_command(fail)

def Survey_Method1(r, l):
    if state.robotType[r] != 'uav':
        alg.do_command(fail)

    alg.do_task('adjustAltitude', r)

    alg.do_command(captureImage, r, 'frontCamera', l)
    
    img = state.currentImage[r]
    position = img['loc']
    person = img['person']
    
    if person != None:
        alg.do_task('rescue', r, person)

    CheckReal(l)

def Survey_Method2(r, l):
    if state.robotType[r] != 'uav':
        alg.do_command(fail)
    
    alg.do_task('adjustAltitude', r)

    alg.do_command(captureImage, r, 'bottomCamera', l)
    
    img = state.currentImage[r]
    position = img['loc']
    person = img['person']
    
    if person != None:
        alg.do_task('rescue', r, person)

    CheckReal(l)

def GetRobot_Method1():
    dist = float("inf")
    robot = None
    for r in rv.WHEELEDROBOTS:
        if state.status[r] == 'free':
            if SR_GETDISTANCE_Euclidean(state.loc[r], (1,1)) < dist:
                robot = r
                dist = SR_GETDISTANCE_Euclidean(state.loc[r], (1,1))
    if robot == None:
        alg.do_command(fail)
    else:
        state.status[robot] = 'busy'
        state.newRobot[1] = robot   # Check if this can cause any regression with assignment statements

def GetRobot_Method2():
    state.newRobot[1] = rv.WHEELEDROBOTS[0]
    state.status[rv.WHEELEDROBOTS[0]] = 'busy'

def AdjustAltitude_Method1(r):
    if state.altitude[r] == 'high':
        alg.do_command(changeAltitude, r, 'low')

def AdjustAltitude_Method2(r):
    if state.altitude[r] == 'low':
        alg.do_command(changeAltitude, r, 'high')
    
def Heuristic2(args):
    r = args[0]
    lfinal = args[1]

    if lfinal == state.loc[r]:
        return float("inf")
    else:
        return 1/SR_GETDISTANCE_Euclidean(state.loc[r], lfinal)

def Heuristic1(args):
    return float("inf")

alg.declare_commands([
    moveEuclidean,
    moveCurved,
    moveManhattan,
    fly,
    giveSupportToPerson,
    clearLocation,
    inspectLocation,
    inspectPerson,
    transfer,
    replenishSupplies,
    captureImage,
    changeAltitude,
    deadEnd,
    fail
    ])

alg.declare_task('moveTo', 'r', 'l')
alg.declare_task('rescue', 'r', 'p')
alg.declare_task('helpPerson', 'r', 'p')
alg.declare_task('getSupplies', 'r')
alg.declare_task('survey', 'r', 'l')
alg.declare_task('getRobot')
alg.declare_task('adjustAltitude', 'r')

alg.declare_methods('moveTo', 
    MoveTo_Method4,
    MoveTo_Method3, 
    MoveTo_Method2, 
    MoveTo_Method1,
    )

alg.declare_methods('rescue',
    Rescue_Method1,
    Rescue_Method2,
    )

alg.declare_methods('helpPerson',
    HelpPerson_Method2,
    HelpPerson_Method1, 
    )

alg.declare_methods('getSupplies',
    GetSupplies_Method2,
    GetSupplies_Method1,
    )

alg.declare_methods('survey',
    Survey_Method1,
    Survey_Method2
    )

alg.declare_methods('getRobot',
    GetRobot_Method1,
    GetRobot_Method2,
    )

alg.declare_methods('adjustAltitude',
    AdjustAltitude_Method1,
    AdjustAltitude_Method2,
    )

if GLOBALS.GetHeuristicName() == 'h1':
    alg.declare_heuristic('survey', Heuristic1)
elif GLOBALS.GetHeuristicName() == 'h2':
    alg.declare_heuristic('survey', Heuristic2)

from env_searchAndRescue import *