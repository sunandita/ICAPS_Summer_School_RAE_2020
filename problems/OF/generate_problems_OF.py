import random
import math
import numpy as np


def generateProblems():
    num = 11
    while num < 112:
        locations = list(range(max(3, int(np.random.normal(6, 2)))))
        locations.append(200)
        factory = frozenset(locations)
        shippingDoc = int(np.random.uniform(0, len(locations) - 2))

        edges = {}

        # set up the edges s.t. the graph is connected
        for loc in locations:
            currEdges = []

            for loc2 in locations:
                if loc != loc2 and loc2 != 200:
                    if np.random.uniform() < 2/len(locations):
                        currEdges.append(loc2)

            if len(currEdges) == 0:
                if loc == 0:
                    currEdges.append(1)
                else:
                    currEdges.append(0)

            if loc == shippingDoc:
                currEdges.append(200)

            edges[loc] = currEdges

        weights = {}


        # make the edges undirected (makes graph strongly connected)
        for loc in edges.keys():
            for dest in edges[loc]:
                if loc not in edges[dest]:
                    edges[dest].append(loc)

        # need to gen weights for all edges (i,j), i<j
        for loc in edges.keys():
            for dest in edges[loc]:
                if loc < dest:
                    weights[(loc, dest)] = max(1, np.random.normal(8,4))


        # set up robots
        robots = []
        robotCapacity = {}

        maxCapacity = 0

        for i in range(max(1, int(np.random.normal(2, 2)))):
            r = 'r' + str(i)
            robots.append(r)
            robotCapacity[r] = np.random.normal(8,2)

            if robotCapacity[r] > maxCapacity:
                maxCapacity = robotCapacity[r]

        # machines
        machines = []
        for i in range(min(len(locations) - 1, max(int(np.random.normal(2,2)), 1))):
            m = 'm' + str(i)
            machines.append(m)

        # pallets
        pallets = []
        for i in range(min(len(locations) - 1, max(int(np.random.normal(2,1)), 1))):
            p = 'p' + str(i)
            pallets.append(p)


        # objects
        objects = []
        obj_weight = {}
        obj_class = {}

        for typeNum in range(max(1, int(np.random.normal(2,1)))):
            type = 'type' + str(typeNum)
            tempType = []

            for i in range(max(1, int(np.random.normal(2,2)))):
                obj = 'o' + str(len(objects))
                objects.append(obj)
                obj_weight[obj] = min(maxCapacity, np.random.normal(7,2))

                tempType.append(obj)

            obj_class[type] = tempType

        stateLoc = {}

        for r in robots:
            stateLoc[r] = np.random.choice(list(factory))
        for m in machines:
            stateLoc[m] = np.random.choice(list(factory))

        busy = {}
        for a in stateLoc.keys():
            busy[a] = False

        numUses = {}
        for m in machines:
            numUses[m] = max(1, int(np.random.normal(10,3)))

        orderTypes = []

        for oc in obj_class.keys():
            for i in range(max(0, min(len(obj_class[oc]), int(np.random.uniform(0,5))))):
                orderTypes.append(oc)

        if orderTypes == []:
            orderTypes.append('type0')

        for p in pallets:
            stateLoc[p] = np.random.choice(list(factory))
        for o in objects:
            stateLoc[o] = np.random.choice(list(factory))

        writeProblem(num, locations, factory, shippingDoc, edges, weights, robots,
                     robotCapacity, machines, objects, obj_weight,
                     obj_class, stateLoc, pallets, busy, numUses, orderTypes)

        num += 1


def writeProblem(num, locations, factory, shippingDoc, edges, weights, robots,
                 robotCapacity, machines, objects, obj_weight,
                 obj_class, stateLoc, pallets, busy, numUses, orderTypes):
    fname = 'auto/problem{}_OF.py'.format(num)
    file = open(fname, "w")
    writeHeader(file)


    file.write("rv.LOCATIONS = " + str(locations) + '\n')
    file.write("rv.FACTORY1 = " + str(factory) + '\n')
    file.write("rv.FACTORY_UNION = rv.FACTORY1\n")
    file.write("rv.SHIPPING_DOC = {rv.FACTORY1: " + str(shippingDoc)+ "}\n\n")

    file.write("rv.GROUND_EDGES = " + str(edges) + '\n')
    file.write("rv.GROUND_WEIGHTS = " + str(weights) + '\n\n')

    # rv.Robots things
    robotString = "rv.ROBOTS = {"
    for r in robots:
        robotString += " '" + r + "': rv.FACTORY1, "
    robotString += "}\n"

    file.write(robotString)

    file.write("rv.ROBOT_CAPACITY = " + str(robotCapacity) + '\n')

    # rv.MACHINES things
    machineString = "rv.MACHINES = {"
    for m in machines:
        machineString += " '" + m + "': rv.FACTORY1, "
    machineString += "}\n"

    file.write(machineString)

    # rv.PALLETS things
    palletString = "rv.PALLETS = {"
    for p in pallets:
        palletString += " '" + p + "', "
    palletString += "}\n"

    file.write(palletString)

    file.write("\n\n")


    file.write("def ResetState():\n")


    # state.OBJECTS things
    objString = "    state.OBJECTS = {"
    for o in objects:
        objString += " '" + o + "': True, "
    objString += "}\n"

    file.write(objString)
    file.write("    state.OBJ_WEIGHT = " + str(obj_weight) + '\n')
    file.write("    state.OBJ_CLASS = " + str(obj_class) + '\n\n')

    stateLocString = "    state.loc = {"
    # state.loc things

    for r in stateLoc.keys():
        stateLocString += " '" + r + "': " + str(stateLoc[r]) + ","

    stateLocString += "}\n"

    file.write(stateLocString)

    # state.load things

    stateLoadString = "    state.load = {"

    for r in robots:
        stateLoadString += " '" + r + "': NIL,"

    stateLoadString += "}\n"

    file.write(stateLoadString)
    file.write("    state.busy = " + str(busy) + '\n')
    file.write("    state.numUses = " + str(numUses) + '\n')

    file.write("    state.var1 = {'temp': 'r0', 'temp1': 'r0', 'temp2': 1, 'redoId': 0}\n")
    file.write("    state.shouldRedo = {}\n\n")

    file.write("tasks = {\n")

    randTimes = random.sample(range(1,2*len(orderTypes)), len(orderTypes))

    # how many tasks you want
    i = 0
    num_tasks = 2

    for idx, o in enumerate(orderTypes):
        if i < num_tasks:
            time = randTimes[idx]
            file.write("    " + str(time) + ": [['orderStart', ['" + str(o) + "']]],\n")
            i += 1
    file.write("}\n")

    file.write("eventsEnv = {\n")
    file.write("}")

    file.close()


def writeHeader(file):
    file.write("__author__ = 'mason'\n\n")
    file.write("from domain_orderFulfillment import *\n")
    file.write("from timer import DURATION\n")
    file.write("from state import state\n")
    file.write("import numpy as np\n\n")

    file.write("\'\'\'\n")
    file.write("This is a randomly generated problem\n")
    file.write("\'\'\'\n\n")

    file.write("def GetCostOfMove(id, r, loc1, loc2, dist):\n")
    file.write("    return 1 + dist\n\n")

    file.write("def GetCostOfLookup(id, item):\n")
    file.write("    return max(1, np.random.beta(2, 2))\n\n")

    file.write("def GetCostOfWrap(id, orderName, m, item):\n")
    file.write("    return max(1, np.random.normal(5, .5))\n\n")

    file.write("def GetCostOfPickup(id, r, item):\n")
    file.write("    return max(1, np.random.normal(4, 1))\n\n")

    file.write("def GetCostOfPutdown(id, r, item):\n")
    file.write("    return max(1, np.random.normal(4, 1))\n\n")

    file.write("def GetCostOfLoad(id, orderName, r, m, item):\n")
    file.write("    return max(1, np.random.normal(3, .5))\n\n")


    file.write("DURATION.TIME = {\n")
    file.write("    'lookupDB': GetCostOfLookup,\n")
    file.write("    'wrap': GetCostOfWrap,\n")
    file.write("    'pickup': GetCostOfPickup,\n")
    file.write("    'putdown': GetCostOfPutdown,\n")
    file.write("    'loadMachine': GetCostOfLoad,\n")
    file.write("    'moveRobot': GetCostOfMove,\n")
    file.write("    'acquireRobot': 1,\n")
    file.write("    'freeRobot': 1,\n")
    file.write("    'wait': 5\n")
    file.write("}\n\n")

    file.write("DURATION.COUNTER = {\n")
    file.write("    'lookupDB': GetCostOfLookup,\n")
    file.write("    'wrap': GetCostOfWrap,\n")
    file.write("    'pickup': GetCostOfPickup,\n")
    file.write("    'putdown': GetCostOfPutdown,\n")
    file.write("    'loadMachine': GetCostOfLoad,\n")
    file.write("    'moveRobot': GetCostOfMove,\n")
    file.write("    'acquireRobot': 1,\n")
    file.write("    'freeRobot': 1,\n")
    file.write("    'wait': 5\n")
    file.write("}\n\n")



if __name__ == "__main__":
    generateProblems()