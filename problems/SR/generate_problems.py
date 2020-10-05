import random
import math

# v8 zero heuristic with timer 1 time
# v7 distance heuristic with timer 1 time
# v6 zero heuristic without timer 5 times
# v5 distance heuristic without timer 5 times
def SR_GETDISTANCE_Manhattan(l0, l1):
    (x1, y1) = l0
    (x2, y2) = l1
    return abs(x2 - x1) + abs(y2 - y1)

def SR_GETDISTANCE_Euclidean(l0, l1):
    (x0, y0) = l0
    (x1, y1) = l1
    return math.sqrt((x1 - x0)*(x1 - x0) + (y1 - y0)*(y1-y0))

def SR_GETDISTANCE_Curved(l0, l1):
    diameter = SR_GETDISTANCE_Euclidean(l0, l1)
    return math.pi * diameter / 2

def GetObstacles(w1_locx, w1_locy, p_locx, p_locy):
    x1 = round((w1_locx + p_locx)/2)
    y1 = round((w1_locy + p_locy)/2)
    circleLength = SR_GETDISTANCE_Curved((w1_locx, w1_locy), (p_locx, p_locy))
    manhattanLength = SR_GETDISTANCE_Manhattan((w1_locx, w1_locy), (p_locx, p_locy))
    if circleLength < manhattanLength:
        r = round(SR_GETDISTANCE_Euclidean((w1_locx, w1_locy), (p_locx, p_locy))/2)
        x2 = x1 + r
        y2 = y1
    else:
        x2 = w1_locx
        y2 = p_locy
    return [(100,100), (x1, y1), (x2, y2)]

def generateProblems():
    num = 19
    for weather in ["clear", "rainy", "dustStorm", "foggy"]:
        for i in range(0, 2):
            p_locx = random.randint(5, 30)
            p_locy = random.randint(5, 30)
            
            w1_locx = random.randint(5, 30)
            w1_locy = random.randint(5, 30)

            w2_locx = random.randint(5, 30)
            w2_locy = random.randint(5, 30)

            a1_locx = random.randint(5, 30)
            a1_locy = random.randint(5, 30)

            obstacles = GetObstacles(w1_locx, w1_locy, p_locx, p_locy)
            for obstacle in obstacles:
                for medicine in ["base", "both"]:
                    for emergency in ["hasDebri", "isInjured"]:
                        writeProblem(num, w1_locx, w1_locy, p_locx, p_locy, w2_locx, w2_locy, 
                            obstacle, medicine, emergency, weather, a1_locx, a1_locy)
                        num += 1

def writeProblem(num, w1_locx, w1_locy, p_locx, p_locy, w2_locx, w2_locy, 
                            obstacle, medicine, emergency, weather, a1_locx, a1_locy):
    fname = 'training/problem{}_SR.py'.format(num)
    file = open(fname,"w") 
    writeHeader(file)
    file.write("rv.OBSTACLES = { ")
    file.write(str(obstacle))
    file.write("}\n\n")

    file.write("def ResetState():\n")
    locString = "    state.loc = {{'w1': ({},{}), 'w2': ({},{}), 'p1': ({},{}), 'a1': ({},{})}}\n".format(
        w1_locx, w1_locy, w2_locx, w2_locy, p_locx, p_locy, a1_locx, a1_locy)
    file.write(locString)

    if medicine == "base":
        medicineString = "    state.hasMedicine = {'a1': 0, 'w1': 0, 'w2': 0}\n"
    elif medicine == "both":
        medicineString = "    state.hasMedicine = {'a1': 0, 'w1': 5, 'w2': 0}\n"
    file.write(medicineString)

    file.write("    state.robotType = {'w1': 'wheeled', 'a1': 'uav', 'w2': 'wheeled'}\n")
    statusString = "    state.status = {{'w1': 'free', 'w2': 'free', 'a1': UNK, 'p1': UNK, ({},{}): UNK}}\n".format(
        p_locx, p_locy)
    file.write(statusString)
    file.write("    state.altitude = {'a1': 'high'}\n")
    file.write("    state.currentImage = {'a1': None}\n")

    if emergency == "hasDebri":
        statusString = "    state.realStatus = {{'w1': 'OK', 'p1': 'OK', 'w2': 'OK', 'a1': OK, ({}, {}): 'hasDebri'}}\n".format(
            p_locx, p_locy)
    elif emergency == "isInjured":
        statusString = "    state.realStatus = {{'w1': 'OK', 'p1': 'injured', 'w2': 'OK', 'a1': OK, ({}, {}): 'clear'}}\n".format(
            p_locx, p_locy)
    file.write(statusString)

    realString = "    state.realPerson = {{({},{}): 'p1'}}\n".format(p_locx, p_locy)
    file.write(realString)

    file.write("    state.newRobot = {1: None}\n")

    weatherString = '    state.weather = {{({},{}): "{}"}}\n\n'.format(p_locx, p_locy, weather)    
    file.write(weatherString)

    file.write("tasks = {\n")
    time = random.randint(1, 8)
    taskString = "    {}: [['survey', 'a1', ({},{})]]\n".format(time, p_locx, p_locy)
    file.write(taskString)
    file.write("}\n")

    file.write("eventsEnv = {\n")
    file.write("}")

    file.close() 

def writeHeader(file):
    file.write("__author__ = 'patras'\n")
    file.write("from domain_searchAndRescue import *\n") 
    file.write("from timer import DURATION\n") 
    file.write("from state import state\n\n") 

    file.write("def GetCostOfMove(r, l1, l2, dist):\n") 
    file.write("    return dist\n\n") 

    file.write("DURATION.TIME = {\n")
    file.write("    'giveSupportToPerson': 15,\n") 
    file.write("    'clearLocation': 5,\n") 
    file.write("    'inspectPerson': 20,\n") 
    file.write("    'moveEuclidean': GetCostOfMove,\n") 
    file.write("    'moveCurved': GetCostOfMove,\n") 
    file.write("    'moveManhattan': GetCostOfMove,\n") 
    file.write("    'fly': 15,\n") 
    file.write("    'inspectLocation': 5,\n") 
    file.write("    'transfer': 2,\n") 
    file.write("    'replenishSupplies': 4,\n") 
    file.write("    'captureImage': 2,\n") 
    file.write("    'changeAltitude': 3,\n") 
    file.write("    'deadEnd': 1,\n")
    file.write("}\n\n") 

    file.write("DURATION.COUNTER = {\n") 
    file.write("    'giveSupportToPerson': 15,\n") 
    file.write("    'clearLocation': 5,\n") 
    file.write("    'inspectPerson': 20,\n") 
    file.write("    'moveEuclidean': GetCostOfMove,\n") 
    file.write("    'moveCurved': GetCostOfMove,\n") 
    file.write("    'moveManhattan': GetCostOfMove,\n") 
    file.write("    'fly': 15,\n") 
    file.write("    'inspectLocation': 5,\n") 
    file.write("    'transfer': 2,\n") 
    file.write("    'replenishSupplies': 4,\n") 
    file.write("    'captureImage': 2,\n") 
    file.write("    'changeAltitude': 3,\n") 
    file.write("    'deadEnd': 1,\n")
    file.write("}\n\n") 
    file.write("rv.WHEELEDROBOTS = ['w1', 'w2']\n")
    file.write("rv.DRONES = ['a1']\n")


if __name__=="__main__":
    generateProblems()