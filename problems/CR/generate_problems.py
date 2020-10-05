import random
import math

#v4 1000 to 1023 search with charging  33 % fail with RAE and 67 % succeed (8 problems)
#v5 1025 to 1051 robot needs to carry charger
#v6 1052 to 1067 Emergency
#v7 1068 to 1099 when charger is with another robot
#v8 1100 to 1123 search with emergency

class Map():
    def __init__(self, initIndex):
        if initIndex == 1:
            self.locations = [1, 2, 3, 4, 5, 6, 7, 8]
            self.edges = {1: [7], 2: [8], 3: [8], 4: [8], 5: [7], 6: [7], 7:[1, 5, 6, 8], 8: [2, 3, 4, 7]}
        elif initIndex == 2:
            self.locations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.edges = {1: [7], 2: [8], 3: [8], 4: [8, 9], 5: [7], 6: [7], 7:[1, 5, 6, 8], 8: [2, 3, 4, 7], 9:[4, 10], 10:[9]}
        elif initIndex == 3:
            self.locations = [1, 2, 3, 4]
            self.edges = {1: [3], 2: [3], 3: [1, 2, 4], 4: [3]}
        elif initIndex == 4:
            self.locations = [1, 2, 3, 4]
            self.edges = {1:[2], 2:[1,3], 3: [2,4], 4:[3]}
        elif initIndex == 5:
            self.locations = [1, 2, 3, 4]
            self.edges = {1:[2, 3], 2:[1,4], 3: [1,4], 4:[2,3]}
        elif initIndex == 6:
            self.locations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.edges = {1:[2], 2:[1,3], 3: [2,4], 4:[5,3, 6, 7], 5:[4, 9], 6:[4, 10], 7:[4, 8], 8:[7], 9:[5], 10:[6]}

    def GetLocationsString(self):
        return "rv.LOCATIONS = " + str(self.locations) + "\n"

    def GetEdgesString(self):
        return "rv.EDGES = " + str(self.edges) + "\n"

    def GetContainerString(self, objLoc):
        containerString = "    state.containers = { "
        for l in self.locations:
            if objLoc == l:
                containerString += str(l) + ":['o1'],"
            else:
                containerString += str(l) + ":[],"
        containerString += "}\n"
        return containerString

MAPS = [Map(1), Map(2), Map(3)]

def generateProblems():
    num = 100
    for cost_index in range(1, 3):
        for map in MAPS:
            for loc in map.locations[1:3]:
                for charge in range(2, 4):
                    for chargerLoc in ['r2', 1]:
                        for j in range(1, 3):
                            obj_loc = random.randint(1, len(map.locations))
                            for pos in [True, False]:
                                for emergency in [True, False]:
                                    writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency)
                                    num += 1

def generateProblemsSearchWithNotEnoughCharge():
    num = 1000
    for cost_index in range(1, 2):
        for map in [Map(3), Map(4), Map(5)]:
            for loc in map.locations:
                charge = 4
                for chargerLoc in [1]:
                    for j in range(1, 3):
                        obj_loc = random.randint(1, len(map.locations))
                        for pos in [False]:
                            for emergency in [False]:
                                writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency)
                                num += 1

def generateProblemsSearchWithEmergency():
    num = 1100
    for cost_index in range(2, 3):
        for map in [Map(3), Map(4), Map(5)]:
            for loc in map.locations:
                charge = 2
                for chargerLoc in [1]:
                    for j in range(1, 3):
                        obj_loc = random.randint(1, len(map.locations))
                        for pos in [False]:
                            for emergency in [True]:
                                writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency)
                                num += 1
    print("num = ", num)

def generateProblemsCarryCharger():
    num = 1025
    for cost_index in range(1, 4):
        for map in [Map(6)]:
            for loc in [1]:
                for charge in range(1, 4):
                    for chargerLoc in [1]:
                        for obj_loc in range(8, 11):
                            for pos in [True]:
                                for emergency in [False]:
                                    writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency)
                                    num += 1

def generateProblemsChargerWithAnotherRobot():
    num = 1068
    for cost_index in range(2, 4):
        for map in [Map(6)]:
            for loc in [1,2]:
                for charge in range(2, 4):
                    for chargerLoc in ['r2']:
                        for obj_loc in range(5, 9):
                            for pos in [True]:
                                for emergency in [False]:
                                    writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency)
                                    num += 1
    print("num = ", num)

def generateProblemsEmergencyWithoutSearch():
    num = 1052
    for cost_index in range(1, 3):
        for map in [Map(1), Map(2)]:
            for loc in [1]:
                for charge in range(2, 4):
                    for chargerLoc in [1]:
                        for j in range(0, 2):
                            obj_loc = random.randint(1, len(map.locations))
                            for pos in [True]:
                                for emergency in [True]:
                                    writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency)
                                    num += 1

def writeProblem(num, map, cost_index, loc, charge, chargerLoc, obj_loc, pos, emergency):
    
    fname = 'training/problem{}_CR.py'.format(num)
    file = open(fname,"w") 
    writeHeader(file, cost_index)

    file.write(map.GetLocationsString())
    file.write(map.GetEdgesString())
    file.write("rv.OBJECTS=['o1']\n\n")

    if chargerLoc == 'r2':
        file.write("rv.ROBOTS=['r1','r2']\n\n")
        locString = "    state.loc = {{'r1': {}, 'r2': {}}}\n".format(loc, 1)
        chargeString = "    state.charge = {{'r1': {}, 'r2': 3}}\n".format(charge)
        loadString = "    state.load = {'r1': NIL, 'r2': NIL}\n"
    else:
        file.write("rv.ROBOTS=['r1']\n\n")
        locString = "    state.loc = {{'r1': {}}}\n".format(loc)
        chargeString = "    state.charge = {{'r1': {}}}\n".format(charge)
        loadString = "    state.load = {'r1': NIL}\n"

    file.write("def ResetState():\n")
    file.write(locString)

    file.write(chargeString)
    
    file.write(loadString)

    if chargerLoc == 'r2':
        chargerLoc = '\'r2\''
    if pos == True:
        posString = "    state.pos = {{'c1': {}, 'o1': {}}}\n".format(chargerLoc, obj_loc)
    else:
        posString = "    state.pos = {{'c1': {}, 'o1': UNK}}\n".format(chargerLoc)

    file.write(posString)
    file.write(map.GetContainerString(obj_loc))

    file.write("    state.emergencyHandling = {'r1': False, 'r2': False}\n")
    file.write("    state.view = {}\n")
    file.write("    for l in rv.LOCATIONS:\n")
    file.write("        state.view[l] = False\n\n")

    file.write("tasks = {\n")
    time = random.randint(1, 8)
    taskString = "    {}: [['fetch', 'r1', 'o1']],\n".format(time)
    file.write(taskString)
    if emergency == True:
        emergencyString = "    {}: [['emergency', 'r1', 2, 1]],\n".format(time+2)
        file.write(emergencyString)
    file.write("}\n")
    
    file.write("eventsEnv = {\n")
    file.write("}")

    file.close() 

def writeHeader(file, index):
    file.write("__author__ = 'patras'\n")
    file.write("from domain_chargeableRobot import *\n") 
    file.write("from timer import DURATION\n") 
    file.write("from state import state\n\n") 

    if index == 1:
        file.write("DURATION.TIME = {\n")
        file.write("    'put': 2,\n") 
        file.write("    'take': 2,\n") 
        file.write("    'perceive': 3,\n") 
        file.write("    'charge': 5,\n") 
        file.write("    'move': 10,\n") 
        file.write("    'moveToEmergency': 5,\n") 
        file.write("    'moveCharger': 15,\n") 
        file.write("    'addressEmergency': 10,\n") 
        file.write("    'wait': 5,\n") 
        file.write("}\n\n") 

        file.write("DURATION.COUNTER = {\n") 
        file.write("    'put': 2,\n") 
        file.write("    'take': 2,\n") 
        file.write("    'perceive': 3,\n") 
        file.write("    'charge': 5,\n") 
        file.write("    'move': 10,\n") 
        file.write("    'moveToEmergency': 5,\n") 
        file.write("    'moveCharger': 15,\n") 
        file.write("    'addressEmergency': 10,\n") 
        file.write("    'wait': 5,\n") 
        file.write("}\n\n") 

    elif index == 2:

        file.write("DURATION.TIME = {\n")
        file.write("    'put': 2,\n") 
        file.write("    'take': 2,\n") 
        file.write("    'perceive': 2,\n") 
        file.write("    'charge': 2,\n") 
        file.write("    'move': 2,\n") 
        file.write("    'moveToEmergency': 2,\n") 
        file.write("    'moveCharger': 2,\n") 
        file.write("    'addressEmergency': 2,\n") 
        file.write("    'wait': 2,\n") 
        file.write("}\n\n") 

        file.write("DURATION.COUNTER = {\n") 
        file.write("    'put': 2,\n") 
        file.write("    'take': 2,\n") 
        file.write("    'perceive': 2,\n") 
        file.write("    'charge': 2,\n") 
        file.write("    'move': 2,\n") 
        file.write("    'moveToEmergency': 2,\n") 
        file.write("    'moveCharger': 2,\n") 
        file.write("    'addressEmergency': 2,\n") 
        file.write("    'wait': 2,\n") 
        file.write("}\n\n") 

    elif index == 3:

        file.write("DURATION.TIME = {\n")
        file.write("    'put': 5,\n") 
        file.write("    'take': 5,\n") 
        file.write("    'perceive': 3,\n") 
        file.write("    'charge': 10,\n") 
        file.write("    'move': 10,\n") 
        file.write("    'moveToEmergency': 20,\n") 
        file.write("    'moveCharger': 15,\n") 
        file.write("    'addressEmergency': 20,\n") 
        file.write("    'wait': 10,\n") 
        file.write("}\n\n") 

        file.write("DURATION.COUNTER = {\n") 
        file.write("    'put': 5,\n") 
        file.write("    'take': 5,\n") 
        file.write("    'perceive': 3,\n") 
        file.write("    'charge': 10,\n") 
        file.write("    'move': 10,\n") 
        file.write("    'moveToEmergency': 20,\n") 
        file.write("    'moveCharger': 15,\n") 
        file.write("    'addressEmergency': 20,\n") 
        file.write("    'wait': 10,\n")  
        file.write("}\n\n") 

if __name__=="__main__":
    generateProblemsSearchWithNotEnoughCharge()
    generateProblemsSearchWithEmergency()
    generateProblemsCarryCharger()
    generateProblemsChargerWithAnotherRobot()
    generateProblemsEmergencyWithoutSearch()