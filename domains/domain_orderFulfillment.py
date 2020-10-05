__author__ = 'mason'

from domain_constants import *
import importlib
#loader = importlib.find_loader('RAE1_and_RAEplan')
#if loader is not None:
import RAE1_and_UPOM as ape
#else:
#    import ape1_and_apeplan as ape

from state import state, rv
import gui
from timer import globalTimer, DURATION
import GLOBALS
import itertools
import random
import numpy as np
from time import time


def fail():
    return FAILURE


# Using Dijsktra's algorithm for ground distance
def OF_GETDISTANCE_GROUND(l0, l1):
    visitedDistances = {l0: 0}
    locs = list(rv.LOCATIONS)

    if l0 == UNK or l0 == NIL or l1 == UNK or l1 == NIL:
        return 10000

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

        for l in rv.GROUND_EDGES[min_loc]:
            if min_loc < l:
                dist = current_dist + rv.GROUND_WEIGHTS[(min_loc, l)]
            else:
                dist = current_dist + rv.GROUND_WEIGHTS[(l, min_loc)]

            if l not in visitedDistances or dist < visitedDistances[l]:
                visitedDistances[l] = dist

    return visitedDistances[l1]


def wait():
    #start = globalTimer.GetTime()
    #while (globalTimer.IsCommandExecutionOver('wait', start) == False):
    #    pass

    if GLOBALS.GetPlanningMode() == True:
        return SUCCESS
    else:
        t1 = time()
        while(time() - t1 < 3):
            pass
        return SUCCESS


def Redoer(command, *args):
    i = 0
    while i < 3:
        if i > 0:
            gui.Simulate("--Redoing command-- %s\n" % command)

        state.var1.AcquireLock('redoId')
        localRedoId = state.var1['redoId']
        state.var1['redoId'] += 1
        state.var1.ReleaseLock('redoId')

        state.shouldRedo[localRedoId] = False
        ape.do_command(command, localRedoId, *args)

        if i > 0:
            gui.Simulate("--Finished redo-- %s\n" % command)

        if not state.shouldRedo.pop(localRedoId):
            break
        i += 1

    if i >= 3:
        ape.do_command(fail)

# this is a function for narrowing down possibilities for obj lists
# e.g. reduces combos for problem 4 task 1 from 10 to 4
def MakeFocusedObjList():
    combos = (itertools.combinations([k for (k,v) in state.OBJECTS.items() if v == True], state.var1['inputLength']))
    focus = []

    orderList = state.var1['input']

    for objList in combos:
        works = True
        for i,objType in enumerate(orderList):
            # verify correct type
            if objList[i] not in state.OBJ_CLASS[objType]:
                works = False
        if works:
            focus.append(objList)

    random.shuffle(focus)

    return focus


# this is a dummy task so we can set the length
# of the order
def OrderStart_Method1(orderList):
    state.var1['inputLength'] = len(orderList)
    state.var1['input'] = orderList
    state.var1['focusObjList'] = MakeFocusedObjList
    ape.do_task('order', orderList)


def Order_Method1(orderList, m, objList):
    if len(orderList) != len(objList):
        gui.Simulate("wrong length objList %s\n" % str(objList))
        ape.do_command(fail)

    # make sure order is of correct type, reserve objects
    for i,objType in enumerate(orderList):
        # verify correct type
        if objList[i] not in state.OBJ_CLASS[objType]:
            gui.Simulate("wrong type %s\n" % str(objList))
            ape.do_command(fail)

        if state.OBJECTS[objList[i]] == False:
            gui.Simulate("obj already used %s\n" % str(objList[i]))
            ape.do_command(fail)

        gui.Simulate("Reserving obj %s\n" % str(objList[i]))
        state.OBJECTS[objList[i]] = False

    # get unique ID for order name
    state.var1.AcquireLock('redoId')
    id = state.var1['redoId']
    state.var1['redoId'] += 1
    state.var1.ReleaseLock('redoId')

    gui.Simulate("This is order ID: " + str(id) + "\n")

    for i, objType in enumerate(orderList):
        # move to object, pick it up, load in machine
        ape.do_task('pickupAndLoad', frozenset([id] + [objList]), objList[i], m)

    # TODO change name wrap to package
    ape.do_task('redoer', wrap, frozenset([id] + [objList]), m, objList)
    package = state.var1['temp1']

    ape.do_task('unloadAndDeliver', m, package)

Order_Method1.parameters = "[(m, objList,) for m in rv.MACHINES for objList in state.var1['focusObjList']()]"


def Order_Method2(orderList, m, objList, p):
    # wait if needed
    if len(orderList) != len(objList):
        gui.Simulate("wrong length %s\n" % str(objList))
        ape.do_command(fail)

    # make sure order is of correct type, reserve objects
    for i,objType in enumerate(orderList):
        # verify correct type
        if objList[i] not in state.OBJ_CLASS[objType]:
            gui.Simulate("wrong type %s\n" % str(objList))
            ape.do_command(fail)

        if state.OBJECTS[objList[i]] == False:
            gui.Simulate("obj already used %s\n" % str(objList))
            ape.do_command(fail)

        state.OBJECTS[objList[i]] = False

    # move objects to the pallet
    for i, objType in enumerate(orderList):
        # move to object, pick it up, place on pallet
        ape.do_task('moveToPallet', objList[i], p)

    # get unique ID for order name
    state.var1.AcquireLock('redoId')
    id = state.var1['redoId']
    state.var1['redoId'] += 1
    state.var1.ReleaseLock('redoId')

    # move objects to machine
    for i,objType in enumerate(orderList):
        # move to object, pick it up, load in machine
        ape.do_task('pickupAndLoad', frozenset([id] + [objList]), objList[i], m)

    # TODO change name wrap to package
    ape.do_task('redoer', wrap, frozenset([id] + [objList]), m, objList)
    package = state.var1['temp1']

    ape.do_task('unloadAndDeliver', m, package)

Order_Method2.parameters = "[(m, objList, p) for m in rv.MACHINES for objList in state.var1['focusObjList']()" \
                           "for p in rv.PALLETS]"


# for free r
def PickupAndLoad_Method1(orderName, o, m, r):
    # wait for robot if needed
    i = 0
    while state.busy[r] == True and i < 5:
        ape.do_command(wait)
        i += 1

    if state.busy[r] == True:
        ape.do_command(fail)

    # acquire robot
    ape.do_task('redoer', acquireRobot, r)

    # move to object
    if state.loc[o] in rv.ROBOTS:
        ape.do_task('redoer', putdown, state.loc[o], o)
    dist = OF_GETDISTANCE_GROUND(state.loc[r], state.loc[o])
    ape.do_task('redoer', moveRobot, r, state.loc[r], state.loc[o], dist)

    # pick up object
    ape.do_task('redoer', pickup, r, o)

    # move to machine
    dist = OF_GETDISTANCE_GROUND(state.loc[r], state.loc[m])
    ape.do_task('redoer', moveRobot, r, state.loc[r], state.loc[m], dist)

    # wait if needed
    i = 0
    while state.busy[m] != False and state.busy[m] != orderName and i < 5:
        ape.do_command(wait)
        i += 1

    if state.busy[m] != False and state.busy[m] != orderName:
        ape.do_command(fail)

    # load machine
    ape.do_task('redoer', loadMachine, orderName, r, m, o)

    ape.do_task('redoer', freeRobot, r)
PickupAndLoad_Method1.parameters = "[(r,) for r in rv.ROBOTS]"


# unload a package from the machine, move package to shipping doc
# for free r
def UnloadAndDeliver_Method1(m, package, r):
    # wait for robot if needed
    i = 0
    while state.busy[r] == True and i < 5:
        ape.do_command(wait)
        i += 1

    if state.busy[r] == True:
        ape.do_command(fail)

    ape.do_task('redoer', acquireRobot, r)

    dist = OF_GETDISTANCE_GROUND(state.loc[r], state.loc[m])
    ape.do_task('redoer', moveRobot, r, state.loc[r], state.loc[m], dist)

    # TODO: may want this to be a different method
    ape.do_task('redoer', pickup, r, package)

    doc = rv.SHIPPING_DOC[rv.ROBOTS[r]]

    dist = OF_GETDISTANCE_GROUND(state.loc[r], doc)
    ape.do_task('redoer', moveRobot, r, state.loc[r], doc, dist)

    ape.do_task('redoer', putdown, r, package)

    ape.do_task('redoer', freeRobot, r)

    gui.Simulate("Package %s has been delivered\n" % package)
UnloadAndDeliver_Method1.parameters = "[(r,) for r in rv.ROBOTS]"


# for free r
def MoveToPallet_Method1(o, p, r):
    # wait for robot if needed
    i = 0
    while state.busy[r] == True and i < 5:
        ape.do_command(wait)
        i += 1

    if state.busy[r] == True:
        ape.do_command(fail)

    ape.do_task('redoer', acquireRobot, r)

    dist = OF_GETDISTANCE_GROUND(state.loc[r], state.loc[o])
    ape.do_task('redoer', moveRobot, r, state.loc[r], state.loc[o], dist)

    ape.do_task('redoer', pickup, r, o)

    dist = OF_GETDISTANCE_GROUND(state.loc[r], state.loc[p])
    ape.do_task('redoer', moveRobot, r, state.loc[r], state.loc[p], dist)

    ape.do_task('redoer', putdown, r, o)
    gui.Simulate("Object %s was placed on pallet %s (goes with earlier msg)\n" % (o, p))

    ape.do_task('redoer', freeRobot, r)
MoveToPallet_Method1.parameters = "[(r,) for r in rv.ROBOTS]"


def moveRobot(redoId, r, l1, l2, dist):
    state.loc.AcquireLock(r)
    state.shouldRedo.AcquireLock(redoId)

    if l1 == l2:
        gui.Simulate("Robot %s is already at location %s\n" %(r, l2))
        res = SUCCESS
        state.shouldRedo[redoId] = False

    elif state.loc[r] == l1:
        start = globalTimer.GetTime()
        while (globalTimer.IsCommandExecutionOver('moveRobot', start, redoId, r, l1, l2, dist) == False):
            pass
        res = Sense('moveRobot')

        if res == SUCCESS:
            gui.Simulate("Robot %s has moved from %s to %s\n" %(r, l1, l2))
            state.loc[r] = l2
            state.shouldRedo[redoId] = False
        else:
            gui.Simulate("Robot %s failed to move due to some internal failure\n" %r)
            state.shouldRedo[redoId] = True
            res = SUCCESS
    else:
        gui.Simulate("Robot %s is not in location %d\n" %(r, l1))
        res = FAILURE
        state.shouldRedo[redoId] = False

    state.shouldRedo.ReleaseLock(redoId)
    state.loc.ReleaseLock(r)

    return res


def pickup(redoId, r, item):
    state.load.AcquireLock(r)
    state.loc.AcquireLock(r)
    state.loc.AcquireLock(item)
    state.shouldRedo.AcquireLock(redoId)

    if r not in rv.ROBOTS or item not in state.OBJECTS:
        gui.Simulate("Passed argument %s or %s isn't a robot or object\n" % (r, item))
        res = FAILURE
        state.shouldRedo[redoId] = False
    elif state.load[r] != NIL:
        gui.Simulate("Robot %s is already carrying an object\n" % r)
        res = FAILURE
        state.shouldRedo[redoId] = False
    elif state.loc[r] != state.loc[item]:
        gui.Simulate("Robot %s and item %s are in different locations\n" % (r, item))
        res = FAILURE
        state.shouldRedo[redoId] = False
    elif state.OBJ_WEIGHT[item] > rv.ROBOT_CAPACITY[r]:
        start = globalTimer.GetTime()
        while (globalTimer.IsCommandExecutionOver('pickup', start, redoId, r, item) == False):
            pass

        gui.Simulate("Item %s is too heavy for robot %s to pick up\n" % (item, r))
        res = FAILURE
        state.shouldRedo[redoId] = False
    else:
        start = globalTimer.GetTime()
        while (globalTimer.IsCommandExecutionOver('pickup', start, redoId, r, item) == False):
            pass
        res = Sense('pickup')

        if res == SUCCESS:
            gui.Simulate("Robot %s picked up %s\n" % (r, item))
            state.loc[item] = r
            state.load[r] = item
            state.shouldRedo[redoId] = False
        else:
            gui.Simulate("Robot %s dropped item %s\n" % (r, item))
            res = SUCCESS
            state.shouldRedo[redoId] = True

    state.shouldRedo.ReleaseLock(redoId)
    state.loc.ReleaseLock(item)
    state.loc.ReleaseLock(r)
    state.load.ReleaseLock(r)

    return res


def putdown(redoId, r, item):
    state.load.AcquireLock(r)
    state.loc.AcquireLock(r)
    state.loc.AcquireLock(item)
    state.shouldRedo.AcquireLock(redoId)

    if state.load[r] != item:
        gui.Simulate("Robot %s is not carrying the object %s\n" % (r, item))
        res = FAILURE
        state.shouldRedo[redoId] = False
    else:
        start = globalTimer.GetTime()
        while (globalTimer.IsCommandExecutionOver('putdown', start, redoId, r, item) == False):
            pass
        res = Sense('putdown')

        if res == SUCCESS:
            gui.Simulate("Robot %s put down %s at loc %s\n" % (r, item, state.loc[r]))
            state.loc[item] = state.loc[r]
            state.load[r] = NIL
            state.shouldRedo[redoId] = False
        else:
            gui.Simulate("Robot %s failed to put down %s\n" % (r, item))
            res = SUCCESS
            state.shouldRedo[redoId] = True

    state.shouldRedo.ReleaseLock(redoId)
    state.loc.ReleaseLock(item)
    state.loc.ReleaseLock(r)
    state.load.ReleaseLock(r)

    return res


def loadMachine(redoId, orderName, r, m, item):
    state.load.AcquireLock(r)
    state.loc.AcquireLock(r)
    state.loc.AcquireLock(m)
    state.loc.AcquireLock(item)
    state.busy.AcquireLock(m)
    state.shouldRedo.AcquireLock(redoId)

    if state.loc[r] != state.loc[m]:
        gui.Simulate("Robot %s isn't at machine %s" % (r, m))
        res = FAILURE
        state.shouldRedo[redoId] = False
    elif state.busy[m] != orderName and state.busy[m] != False:
        gui.Simulate("Robot %s can't load machine %s, it is working on a different order\n" %(r, m,))
        res = FAILURE
        state.shouldRedo[redoId] = False
    else:
        start = globalTimer.GetTime()
        while (globalTimer.IsCommandExecutionOver('loadMachine', start, redoId, orderName, r, m, item) == False):
            pass

        res = Sense('loadMachine')

        if res == SUCCESS:
            gui.Simulate("Robot %s loaded machine %s with item %s\n" % (r, m, item))
            state.load[r] = NIL
            state.loc[item] = m

            state.busy[m] = orderName
            state.shouldRedo[redoId] = False
        else:
            gui.Simulate("Robot %s failed to load machine %s\n" % (r, m))
            res = SUCCESS
            state.shouldRedo[redoId] = True

    state.shouldRedo.ReleaseLock(redoId)
    state.busy.ReleaseLock(m)
    state.loc.ReleaseLock(item)
    state.loc.ReleaseLock(m)
    state.loc.ReleaseLock(r)
    state.load.ReleaseLock(r)

    return res



# to be not busy anymore, or drop object
def acquireRobot(redoId, r):
    state.busy.AcquireLock(r)
    state.load.AcquireLock(r)
    state.shouldRedo.AcquireLock(redoId)

    state.shouldRedo[redoId] = False

    if state.busy[r] == True:
        gui.Simulate("Robot %s is busy\n" % r)
        res = FAILURE
    elif state.load[r] != NIL:
        gui.Simulate("Robot %s is carrying an object\n" % r)
        res = FAILURE
    else:
        gui.Simulate("Robot %s is acquired for a new task\n" % r)
        state.busy[r] = True
        res = SUCCESS

    state.shouldRedo.ReleaseLock(redoId)
    state.load.ReleaseLock(r)
    state.busy.ReleaseLock(r)

    return res


def freeRobot(redoId, r):
    state.busy.AcquireLock(r)
    state.load.AcquireLock(r)
    state.shouldRedo.AcquireLock(redoId)

    state.shouldRedo[redoId] = False

    if state.load[r] != NIL:
        gui.Simulate("Robot %s is carrying an object\n" % r)
        res = FAILURE
    else:
        gui.Simulate("Robot %s is now free\n" % r)
        state.busy[r] = False
        res = SUCCESS

    state.shouldRedo.ReleaseLock(redoId)
    state.load.ReleaseLock(r)
    state.busy.ReleaseLock(r)

    return res


def wrap(redoId, orderName, m, objList):
    state.loc.AcquireLock(m)
    state.busy.AcquireLock(m)
    state.numUses.AcquireLock(m)
    state.shouldRedo.AcquireLock(redoId)

    weight = 0

    for obj in objList:
        weight += state.OBJ_WEIGHT[obj]
        if state.loc[obj] != m:
            gui.Simulate("Machine %s not loaded with item %s\n" % (m, obj))
            res = FAILURE
            state.shouldRedo[redoId] = False

            state.shouldRedo.ReleaseLock(redoId)
            state.numUses.ReleaseLock(m)
            state.busy.ReleaseLock(m)
            state.loc.ReleaseLock(m)

            return res

    if state.busy[m] != orderName:
        gui.Simulate("Machine %s is busy with a differnt order\n" % m)
        res = FAILURE
        state.shouldRedo[redoId] = False
    else:
        start = globalTimer.GetTime()
        while globalTimer.IsCommandExecutionOver('wrap', start, redoId, orderName, m, objList) == False:
            pass

        state.numUses[m] += 1
        res = SenseWrap(state.numUses[m])

        if res == SUCCESS:
            # TODO better, unique name
            packageName = "Pack#" + str(orderName)

            state.OBJECTS[packageName] = True
            state.loc[packageName] = state.loc[m]
            state.OBJ_WEIGHT[packageName] = weight


            state.var1.AcquireLock('temp1')
            state.var1['temp1'] = packageName
            state.var1.ReleaseLock('temp1')

            gui.Simulate("Machine %s wrapped package %s\n" % (m, packageName))
            state.busy[m] = False
            state.shouldRedo[redoId] = False


        else:
            gui.Simulate("Machine %s jammed. Failed to wrap\n" % m)
            state.shouldRedo[redoId] = True
            # set res to success for return
            res = SUCCESS

    state.shouldRedo.ReleaseLock(redoId)
    state.numUses.ReleaseLock(m)
    state.busy.ReleaseLock(m)
    state.loc.ReleaseLock(m)

    return res


# Define heuristics (returns expected efficiency for external tasks)
def Heuristic1(args):
    return float("inf")


def Heuristic2(args):
    order = args[0]
    totalDist = 1
    for itemClass in order:
        minDist = float("inf")
        for item in state.OBJ_CLASS[itemClass]:
            loc = state.loc[item]
            if loc not in rv.LOCATIONS:
                loc = state.loc[loc]
            temp = OF_GETDISTANCE_GROUND(loc, rv.SHIPPING_DOC[rv.FACTORY1])
            if temp < minDist:
                minDist = temp

        totalDist += minDist
    return 100/totalDist


if GLOBALS.GetHeuristicName() == 'h1':
    ape.declare_heuristic('orderStart', Heuristic1)
elif GLOBALS.GetHeuristicName() == 'h2':
    ape.declare_heuristic('orderStart', Heuristic2)


# Declare tasks
ape.declare_task('orderStart', 'orderList')
ape.declare_task('order', 'orderList')
ape.declare_task('pickupAndLoad', 'orderName', 'o', 'm')
ape.declare_task('unloadAndDeliver', 'm', 'package')
ape.declare_task('moveToPallet', 'o', 'p')
ape.declare_task('redoer', 'command')

ape.declare_methods('orderStart', OrderStart_Method1)
ape.declare_methods('order', Order_Method1, Order_Method2)
ape.declare_methods('pickupAndLoad', PickupAndLoad_Method1)
ape.declare_methods('unloadAndDeliver', UnloadAndDeliver_Method1)
ape.declare_methods('moveToPallet', MoveToPallet_Method1)
ape.declare_methods('redoer', Redoer)

ape.declare_commands([fail, wrap, pickup, acquireRobot,
                      loadMachine, moveRobot, freeRobot, putdown,
                      wait])


from env_orderFulfillment import *


