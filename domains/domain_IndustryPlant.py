__author__ = 'patras'

from RAE1_and_RAEplan import *

from state import state, rv
from gui import Simulate
from domain_constants import *
from timer import globalTimer


# Using Dijsktra's algorithm
def IP_GETDISTANCE(l0, l1):
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

# Using Dijsktra's algorithm
def IP_GETPATH(l0, l1):
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

def fail():
    return FAILURE

def damage(*machines):
    for m in machines:
        state.cond.AcquireLock(m)
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('damage', start) == False):
            pass
        Simulate("Machine %s is damaged\n" %m)
        state.cond[m] = NOTOK
        state.cond.ReleaseLock(m)
    return SUCCESS

def repairc(m):
    state.cond.AcquireLock(m)
    start = globalTimer.GetTime()
    while(globalTimer.IsCommandExecutionOver('repairc', start) == False):
        pass
    Simulate("Machine %s is repaired\n" %m)
    state.cond[m] = OK
    state.cond.ReleaseLock(m)
    return SUCCESS

def GetNewName():
    state.name.AcquireLock('counter')
    state.name['counter'] += 1
    state.name.ReleaseLock('counter')
    newName = 'TMPOBJECT' + state.name['counter'].__str__()
    return newName

def paint(m, o, colour, name):
    state.pos.AcquireLock(o)
    if state.pos[o] == rv.MACHINE_LOCATION[m]:
        if state.cond[m] == OK:
            state.status.AcquireLock(m)
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('paint', start) == False):
                pass
            res = Sense('paint')
            if res == SUCCESS:
                state.pos[name] = rv.MACHINE_LOCATION[m]
                state.status[m] = 'free'
            else:
                Simulate("Painting has failed due to an internal failure.\n")
            state.status.ReleaseLock(m)
        else:
            Simulate("%s is damaged\n" %m)
            res = FAILURE

    else:
        Simulate("object not in machine location", o, m, rv)
        res = FAILURE
    state.pos.ReleaseLock(o)
    return res

def wrap(m, o, name):
    state.pos.AcquireLock(o)
    if state.pos[o] == rv.MACHINE_LOCATION[m]:
        if state.cond[m] == OK:
            state.status.AcquireLock(m)
            Simulate("%s is wrapping %s and naming it %s\n" %(m, o, name))
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('wrap', start) == False):
                pass
            res = Sense('wrap')
            if res == SUCCESS:
                state.pos[name] = rv.MACHINE_LOCATION[m]
                state.status[m] = 'free'
            else:
                Simulate("Wrapping failed due to some internal failure\n")
            state.status.ReleaseLock(m)
        else:
           Simulate("%s is damaged\n" %m)
           res = FAILURE
    else:
        Simulate("%s is not in wrapping machine's location\n" %o)
        res = FAILURE
    state.pos.ReleaseLock(o)
    return res

def assemble(m, p1, p2, name):
    state.pos.AcquireLock(p1)
    state.pos.AcquireLock(p2)

    if state.pos[p1] == rv.MACHINE_LOCATION[m] and state.pos[p2] == rv.MACHINE_LOCATION[m]:
        if state.cond[m] == OK:
            state.status.AcquireLock(m)
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('assemble', start) == False):
                pass
            res = Sense('assemble')
            if res == SUCCESS:
                Simulate("Assembled parts %s and %s and naming it %s\n" %(p1, p2, name))
                state.pos[name] = rv.MACHINE_LOCATION[m]
                state.status[m] = 'free'
            else:
                Simulate("Assemble failed due to some internal failure.\n")
            state.status.ReleaseLock(m)
        else:
           Simulate("%s is damaged\n" %m)
           res = FAILURE
    else:
        Simulate("Part %s or %s is not in painting machine's location\n" %(p1, p2))
        res = FAILURE
    state.pos.ReleaseLock(p1)
    state.pos.ReleaseLock(p2)
    return res

def pack(m, o1, o2, name):
    state.pos.AcquireLock(o1)
    state.pos.AcquireLock(o2)
    if state.pos[o1] == rv.MACHINE_LOCATION[m] and state.pos[o2] == rv.MACHINE_LOCATION[m]:
        if state.cond[m] == OK:
            state.status.AcquireLock(m)
            start = globalTimer.GetTime()
            while(globalTimer.IsCommandExecutionOver('pack', start) == False):
                pass
            res = Sense('pack')
            if res == SUCCESS:
                Simulate("Packed objects %s and %s and naming it %s\n" %(o1, o2, name))
                state.pos[name] = rv.MACHINE_LOCATION[m]
            else:
                Simulate("pack failed due to some internal failure.\n")
            state.status.ReleaseLock(m)
        else:
           Simulate("%s is damaged\n" %m)
           res = FAILURE
    else:
        Simulate("Part %s or %s is not in packing machine's location\n" %(o1, o2))
        res = FAILURE
    state.pos.ReleaseLock(o1)
    state.pos.ReleaseLock(o2)
    return res

def take(r, o, l):
    state.pos.AcquireLock(o)
    if state.pos[o] == l:
        state.load.AcquireLock(r)
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('take', start) == False):
            pass
        res = Sense('take')
        if res == SUCCESS:
            state.pos[o] = r
            state.load[r] = o
            Simulate("Robot %s has taken object %s at location %d\n" %(r,o,l))
        else:
            Simulate("Take has failed due to an internal failure.\n")
        state.load.ReleaseLock(r)
    else:
        Simulate("Object %s is not at location %d\n" %(o,l))
        res = FAILURE
    state.pos.ReleaseLock(o)
    return res

def put(r, o, l):
    state.pos.AcquireLock(o)
    if state.pos[o] == r:
        state.load.AcquireLock(r)
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('put', start) == False):
            pass
        res = Sense('put')
        if res == SUCCESS:
            state.pos[o] = l
            state.load[r] = NIL
            Simulate("Robot %s has put object %s at location %d\n" %(r,o,l))
        else:
            Simulate("put has failed due to some internal failure.\n")
        state.load.ReleaseLock(r)
    else:
        Simulate("Object %s is not with robot %s\n" %(o,r))
        res = FAILURE
    state.pos.ReleaseLock(o)
    return res

def move(r, loc1, loc2):
    state.loc.AcquireLock(r)
    if state.loc[r] == loc1:
        start = globalTimer.GetTime()
        while(globalTimer.IsCommandExecutionOver('move', start) == False):
            pass
        res = SenseMove(loc1)
        if res == SUCCESS:
            state.loc[r] = loc2
            #Simulate("%s has moved from %s to %s\n" %(r, loc1, loc2))
            Simulate('move', r, loc1, loc2, "\n")
        else:
            Simulate("Move of %s has failed due to some internal failure.\n" %r)
    else:
        #Simulate("%s is not in location %s\n" %(r, loc1))
        Simulate("not in location", r, loc1)
        res = FAILURE
    state.loc.ReleaseLock(r)
    return res

def Delegate(o, o_name):
    taskName = o[0]
    taskArgs = o[1:]
    do_task(taskName, o_name, *taskArgs)

def GetMachine(job, loc):
    free = [m for m in rv.MACHINES[job] if state.status[m] == 'free']
    if loc in rv.ROBOTS:
        r = loc
        do_command(put, r, state.load[r], state.loc[r])
        loc = state.loc[r]
    dist = [IP_GETDISTANCE(loc, rv.MACHINE_LOCATION[m]) for m in free]
    if free == []:
        return NIL
    else:
        return free[dist.index(min(dist))]

def GetLocation(o):
    if o not in state.pos:
        state.pos[o] = rv.BUFFERS['input']
    return state.pos[o]

def Paint_Method1(name, *args):
    o = args[0]
    colour = args[1]
    if isinstance(o, list):
        o_name = GetNewName()
        Delegate(o, o_name)
    else:
        o_name = o

    m = GetMachine('paint', GetLocation(o_name))
    if m != NIL:
        if state.cond[m] == OK:
            if GetLocation(o_name) != rv.MACHINE_LOCATION[m]:
                do_task('deliver', o_name, rv.MACHINE_LOCATION[m])
            do_command(paint, m, o_name, colour, name)
        else:
            Simulate("Machine %s for painting is damaged " %m)
            do_command(fail)
    else:
        Simulate("There are no machines free to paint.\n")
        do_command(fail)

def Paint_Method2(name, *args):
    "repairs machine if it is damaged"
    o = args[0]
    colour = args[1]
    if isinstance(o, list):
        o_name = GetNewName()
        Delegate(o, o_name)
    else:
        o_name = o

    m = GetMachine('paint', GetLocation(o_name))
    if m != NIL:
        if state.cond[m] == NOTOK:
            do_task('repair', m)
        if GetLocation(o_name) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name, rv.MACHINE_LOCATION[m])
        do_command(paint, m, o_name, colour, name)
    else:
        Simulate("There are no machines free to paint.\n")
        do_command(fail)

def Assemble_Method2(name, *args):
    part1 = args[0]
    part2 = args[1]
    if isinstance(part1, list):
        o_name1 = GetNewName()
        Delegate(part1, o_name1)
    else:
        o_name1 = part1

    if isinstance(part2, list):
        o_name2 = GetNewName()
        Delegate(part2, o_name2)
    else:
        o_name2 = part2

    m = GetMachine('assemble', GetLocation(o_name1))
    if m != NIL:
        if state.cond[m] == NOTOK:
            do_task('repair', m)
        if GetLocation(o_name1) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name1, rv.MACHINE_LOCATION[m])
        if GetLocation(o_name2) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name2, rv.MACHINE_LOCATION[m])
        do_command(assemble, m, o_name1, o_name2, name)
    else:
        Simulate("There are no machines free to assemble.\n")
        do_command(fail)

def Assemble_Method1(name, *args):
    part1 = args[0]
    part2 = args[1]
    if isinstance(part1, list):
        o_name1 = GetNewName()
        Delegate(part1, o_name1)
    else:
        o_name1 = part1

    m = GetMachine('assemble', GetLocation(o_name1))
    if m != NIL:
        if state.cond[m] == NOTOK:
            do_task('repair', m)
        if GetLocation(o_name1) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name1, rv.MACHINE_LOCATION[m])
    else:
        Simulate("There are no machines free to assemble.\n")
        return FAILURE

    if isinstance(part2, list):
        o_name2 = GetNewName()
        Delegate(part2, o_name2)
    else:
        o_name2 = part2

    if GetLocation(o_name2) != rv.MACHINE_LOCATION[m]:
        do_task('deliver', o_name2, rv.MACHINE_LOCATION[m])

    do_command(assemble, m, o_name1, o_name2, name)

def Pack_Method2(name, *args):
    o1 = args[0]
    o2 = args[1]
    if isinstance(o1, list):
        o_name1 = GetNewName()
        Delegate(o1, o_name1)
    else:
        o_name1 = o1

    if isinstance(o2, list):
        o_name2 = GetNewName()
        Delegate(o2, o_name2)
    else:
        o_name2 = o2

    m = GetMachine('pack', GetLocation(o_name1))
    if m != NIL:
        if state.cond[m] == NOTOK:
            do_task('repair', m)
        if GetLocation(o_name1) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name1, rv.MACHINE_LOCATION[m])
        if GetLocation(o_name2) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name2, rv.MACHINE_LOCATION[m])
        do_command(pack, m, o_name1, o_name2, name)
    else:
        Simulate("There are no machines free to pack.\n")
        do_command(fail)

def Pack_Method1(name, *args):
    o1 = args[0]
    o2 = args[1]
    if isinstance(o1, list):
        o_name1 = GetNewName()
        Delegate(o1, o_name1)
    else:
        o_name1 = o1

    m = GetMachine('pack', GetLocation(o_name1))
    if m != NIL:
        if state.cond[m] == NOTOK:
            do_task('repair', m)
    else:
        Simulate("There are no machines free to pack.\n")
        do_command(fail)

    if GetLocation(o_name1) != rv.MACHINE_LOCATION[m]:
        do_task('deliver', o_name1, rv.MACHINE_LOCATION[m])

    if isinstance(o2, list):
        o_name2 = GetNewName()
        Delegate(o2, o_name2)
    else:
        o_name2 = o2

    if GetLocation(o_name2) != rv.MACHINE_LOCATION[m]:
        do_task('deliver', o_name2, rv.MACHINE_LOCATION[m])
    do_command(pack, m, o_name1, o_name2, name)

def Wrap_Method1(name, o):
    if isinstance(o, list):
        o_name = GetNewName()
        Delegate(o, o_name)
    else:
        o_name = o

    m = GetMachine('wrap', GetLocation(o_name))
    if m != NIL:
        if GetLocation(o_name) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name, rv.MACHINE_LOCATION[m])
        do_command(wrap, m, o_name, name)
    else:
        Simulate("There are no machines free to wrap.\n")
        do_command(fail)

def Wrap_Method2(name, o):
    if isinstance(o, list):
        o_name = GetNewName()
        Delegate(o, o_name)
    else:
        o_name = o

    m = GetMachine('wrap', GetLocation(o_name))
    if m != NIL:
        do_task('repair', m)
        if GetLocation(o_name) != rv.MACHINE_LOCATION[m]:
            do_task('deliver', o_name, rv.MACHINE_LOCATION[m])
        do_command(wrap, m, o_name, name)
    else:
        Simulate("There are no machines free to wrap.\n")
        do_command(fail)

def Order_Method1(taskArgs):
    taskName = taskArgs[0]
    args = taskArgs[1:]
    name = GetNewName()
    do_task(taskName, name, *args)
    do_task('deliver', name, rv.BUFFERS['output'])

#def GetRobot_Method3(loc):
#   free = [r for r in rv.ROBOTS if state.status[r] == 'free']
#    dist = [IP_GETDISTANCE(loc, state.loc[r]) for r in free]
#    if dist != []:
#        r = free[dist.index(min(dist))]
#        state.status[r] = 'busy'
#        state.deliveryRobot[0] = r
#    else:
#        do_command(fail)

def GetRobot_Method1(loc):
    r = rv.ROBOTS[0]
    if state.status[r] == 'busy':
        Simulate("No robot is free to deliver to location %s\n" %(loc))
        do_command(fail)
    else:
        state.deliveryRobot[0] = r

def GetRobot_Method2(loc):
    r = rv.ROBOTS[1]
    if state.status[r] == 'busy':
        Simulate("No robot is free to deliver to location %s\n" %(loc))
        do_command(fail)
    else:
        state.deliveryRobot[0] = r

def GetRobot_Method3(loc):
    r = rv.ROBOTS[2]
    if state.status[r] == 'busy':
        Simulate("No robot is free to deliver to location %s\n" %(loc))
        do_command(fail)
    else:
        state.deliveryRobot[0] = r

# def GetRobot_Method1(loc):
#     free = [r for r in rv.ROBOTS if state.status[r] == 'free']
#     dist = [IP_GETDISTANCE(loc, state.loc[r]) for r in free]
#     if dist != []:
#         r = free[dist.index(min(dist))]
#         deliveryRobot = r
#         state.status[r] = 'busy'
#     else:
#         deliveryRobot = NIL
#     return deliveryRobot

def Deliver_Method1(o, l):
    loc_o = GetLocation(o)
    if loc_o in rv.LOCATIONS:
        do_task('getRobot', loc_o)
        deliveryRobot = state.deliveryRobot[0]
        if state.loc[deliveryRobot] != loc_o:
            do_task('moveTo', deliveryRobot, state.loc[deliveryRobot], loc_o)
        do_command(take, deliveryRobot, o, loc_o)
        if state.loc[deliveryRobot] != l:
            do_task('moveTo', deliveryRobot, state.loc[deliveryRobot], l)
        do_command(put, deliveryRobot, o, l)
        state.status[deliveryRobot] = 'free'
    else:
        Simulate("Some robot is carrying the object %s \n" %o)
        do_command(fail)

def Deliver_Method2(o, l):
    loc_o = GetLocation(o)
    if loc_o in rv.ROBOTS:
        r = loc_o
        do_task('moveTo', r, state.loc[r], l)
        do_command(put, r, o, l)
        state.status[r] = 'free'
    else:
        Simulate("Object %s is not with any robot. \n" %o)
        do_command(fail)

def Repair_Method1(m):
    do_task('getRobot', rv.MACHINE_LOCATION[m])
    repairBot = state.deliveryRobot[0]
    if repairBot != NIL:
        if state.loc[repairBot] != rv.MACHINE_LOCATION[m]:
            do_task('moveTo', repairBot, state.loc[repairBot], rv.MACHINE_LOCATION[m])
        do_command(repairc, m)
        state.status[repairBot] = 'free'
    else:
        Simulate("No robot is free to repair %s\n" %m)
        do_command(fail)

def MoveTo_Method1(r, l1, l2):
    path = IP_GETPATH(l1, l2)
    if path == {}:
        Simulate("%s is already at location %s \n" %(r, l2))
    else:
        lTemp = state.loc[r]
        if lTemp not in path:
            Simulate("%s is out of its path to %s\n" %(r, l2))
            do_command(fail)
        else:
            while(lTemp != l2):
                lNext = path[lTemp]
                do_command(move, r, lTemp, lNext)
                if lNext != state.loc[r]:
                    Simulate("%s is out of its path to %s\n" %(r, l2))
                    do_command(fail)
                else:
                    lTemp = lNext

declare_task('paint', '*')
declare_task('assemble', '*')
declare_task('pack', '*')
declare_task('wrap', '*')
declare_task('deliver', 'o', 'l')
declare_task('order', 'taskArgs')
declare_task('repair', 'm')
declare_task('moveTo', 'r', 'l1', 'l2')
declare_task('getRobot', 'loc')   

declare_commands([
    paint, 
    assemble, 
    pack, 
    take, 
    put, 
    move, 
    wrap, 
    repairc,
    fail])

declare_methods('paint', Paint_Method1, Paint_Method2)
declare_methods('assemble', Assemble_Method1, Assemble_Method2)
declare_methods('pack', Pack_Method1, Pack_Method2)
declare_methods('wrap', Wrap_Method1, Wrap_Method2)
declare_methods('deliver', Deliver_Method1, Deliver_Method2)
declare_methods('order', Order_Method1)
declare_methods('repair', Repair_Method1)
declare_methods('moveTo', MoveTo_Method1)
declare_methods('getRobot', GetRobot_Method1, GetRobot_Method2, GetRobot_Method3)

def Heuristic1(args):
    return float("inf")

def Heuristic2(args):
    return 

if GLOBALS.GetHeuristicName() == 'h1':
    declare_heuristic('order', Heuristic1)
    
from env_IndustryPlant import *