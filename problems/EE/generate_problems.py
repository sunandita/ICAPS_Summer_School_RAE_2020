import random
import math

def EE_GETDISTANCE(l0, l1, locs, edges):
    visitedDistances = {l0: 0}
    locs = list(locs)

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

        for l in edges[min_loc]:
            dist = current_dist + edges[min_loc][l]
            if l not in visitedDistances or dist < visitedDistances[l]:
                visitedDistances[l] = dist

    return visitedDistances[l1]

class Map():
    def __init__(self, initIndex):
        if initIndex == 1:
            self.locations = ['base', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7']
            self.edges = {
                'base': {
                    'z1': 15,
                    'z4': 15,
                    'z5': 35,
                    'z6': 35,
                    'z7': 35
                },
                'z1': {
                    'base': 15,
                    'z2': 30
                },
                'z2': {
                    'z1': 30,
                    'z3': 30
                },
                'z3': {
                    'z2': 30,
                    'z4': 30
                },
                'z4': {
                    'z3': 30,
                    'base': 15
                },
                'z5': {
                    'base': 35
                },
                'z6': {
                    'base': 35
                },
                'z7': {
                    'base': 35
                }
            }
        elif initIndex == 2:
            self.locations = ['base', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6']
            self.edges = {
                'base': {
                    'z1': 50,
                    'z3': 50,
                    'z4': 40,
                    'z6': 40,
                },
                'z1': {
                    'base': 50,
                    'z2': 20
                },
                'z2': {
                    'z1': 20,
                    'z3': 20
                },
                'z3': {
                    'z2': 20,
                    'base': 50
                },
                'z4': {
                    'z3': 90,
                    'z5': 35
                },
                'z5': {
                    'z4': 35,
                    'z6': 35,
                },
                'z6': {
                    'base': 40,
                    'z5': 35,
                }
            }

        elif initIndex == 3:
            self.locations = ['base', 'z1', 'z2', 'z3', 'z4']
            self.edges = {
                'base': {
                    'z1': 20,
                    'z2': 50,
                    'z3': 20,
                    'z4': 50
                },
                'z1': {
                    'base': 20,
                    'z2': 30,
                    'z4': 50
                },
                'z2': {
                    'base': 50,
                    'z1': 30,
                    'z3': 30
                },
                'z3': {
                    'base': 20,
                    'z2': 30,
                    'z4': 30
                },
                'z4': {
                    'base': 50,
                    'z3': 30,
                    'z1': 50
                }
            }

    def GetLocationsString(self):
        return "rv.LOCATIONS = " + str(self.locations) + "\n"

    def GetEdgesString(self):
        return "rv.EDGES = " + str(self.edges) + "\n"

MAPS = [Map(1), Map(2), Map(3)]

def generateProblems():
    num = 100
    for map1 in MAPS: # 3 
        charge1 = [random.choice([50, 80]), random.choice([50, 80]), random.choice([50, 80])] # uav, r1, r2
        charge2 = [random.choice([50, 80]), random.choice([50, 80]), random.choice([50, 80])]
        if charge1[0] == 50:
            charge2[0] = 80
        else:
            charge2[0] = 50 # making them different
        for charge in [charge1, charge2]:
            chargerLoc = random.choice(map1.locations) # 1

            data1 = [random.choice([1, 3]), random.choice([3, 1]), random.choice([1, 3])]
            data2 = [random.choice([1, 3]), random.choice([3, 1]), random.choice([1, 3])]
            if data1[0] == 1:
                data2[0] = 3
            else:
                data2[0] = 1 # making them different
            for data in [data1, data2]:
                weather = random.choice(['normal', 'stormy'])
                for load in [True, False]:
                    for equipmentLoc in ['base', 'r2']:
                        for emergency in [True, False]: # 2
                            for numTasks in [1,2]: # 2
                                writeProblem(num, map1, charge, chargerLoc, equipmentLoc, data, weather, load, emergency, numTasks)
                                num += 1

def GetRandomJob():
    return random.choice(['survey', 'monitor', 'sample', 'process', 'screen'])

def GetLocs(locations, edges, count):
    loc0 = 'base'
    locs = []
    i = 0
    while(i < count):
        l = random.choice(locations)
        if l not in locs and l != loc0:
            if EE_GETDISTANCE(loc0, l, locations, edges) < 100:
                i += 1
                locs.append(l)
                loc0 = l
    return locs

EQUIPMENT = {'survey': 'e1', 'monitor': 'e2', 'screen': 'e3', 'sample': 'e4', 'process': 'e5'}

def writeProblem(num, map, charge, chargerLoc, equipmentLoc, data, weather, load, emergency, numTasks):
    
    fname = 'training/problem{}_EE.py'.format(num)
    file = open(fname,"w") 
    writeHeader(file)

    file.write("rv.TYPE = {'e1': 'survey', 'e2': 'monitor', 'e3': 'screen', 'e4': 'sample', 'e5':'process'}\n")
    file.write("rv.EQUIPMENT = {'survey': 'e1', 'monitor': 'e2', 'screen': 'e3', 'sample': 'e4', 'process': 'e5'}\n")
    file.write("rv.EQUIPMENTTYPE = {'e1': 'survey', 'e2': 'monitor', 'e3': 'screen', 'e4': 'sample', 'e5':'process'}\n")
    file.write(map.GetLocationsString())
    file.write(map.GetEdgesString())

    file.write("\ndef ResetState():\n")
    file.write("    state.loc = {'r1': 'base', 'r2': 'base', 'UAV': 'base'}\n")
    
    chargeString = "    state.charge = {{ 'UAV': {}, 'r1': {}, 'r2': {}}}\n".format(charge[0], charge[1], charge[2])
    file.write(chargeString)
    dataString = "    state.data = {{ 'UAV': {}, 'r1': {}, 'r2': {}}}\n".format(data[0], data[1], data[2])
    file.write(dataString)

    if numTasks == 1:
        jobs1 = ['survey', 'survey', 'survey']
        jobs1Locs = GetLocs(map.locations, map.edges, 3)
        e1 = EQUIPMENT[jobs1[0]]
    else:
        jobs1 = ['survey', 'survey']
        jobs1Locs = GetLocs(map.locations, map.edges, 2)
        e1 = EQUIPMENT[jobs1[0]]
        jobs2 = [GetRandomJob(), GetRandomJob(), GetRandomJob()]
        jobs2Locs = GetLocs(map.locations, map.edges, 3)

    if load == False:
            if equipmentLoc == 'r2':
                loadString = "    state.load = {{'r1': NIL, 'r2': '{}', 'UAV': NIL}}\n".format(e1)  
                posDict = {
                    'c1': 'base',
                    'e1': 'base',
                    'e2': 'base',
                    'e3': 'base',
                    'e4': 'base',
                    'e5': 'base',
                }  
                posDict[e1] = 'r2'
                posString = "    state.pos = " + str(posDict) + "\n"
            else:
                loadString = "    state.load = {'r1': NIL, 'r2': NIL, 'UAV': NIL}\n"
                posDict = {
                    'c1': 'base',
                    'e1': 'base',
                    'e2': 'base',
                    'e3': 'base',
                    'e4': 'base',
                    'e5': 'base',
                }  
                posString = "    state.pos = " + str(posDict) + "\n"
    else:
        if equipmentLoc == 'r2':
            loadString = "    state.load = {{'r1': NIL, 'r2': '{}', 'UAV': 'o1'}}\n".format(e1)
            posDict = {
                    'c1': 'base',
                    'e1': 'base',
                    'e2': 'base',
                    'e3': 'base',
                    'e4': 'base',
                    'e5': 'base',
                    'o1': 'UAV',
                }  
            posDict[e1] = 'r2'
            posString = "    state.pos = " + str(posDict) + "\n"
        else:
            loadString = "    state.load = {'r1': NIL, 'r2': NIL, 'UAV': 'o1'}\n"
            posDict = {
                    'c1': 'base',
                    'e1': 'base',
                    'e2': 'base',
                    'e3': 'base',
                    'e4': 'base',
                    'e5': 'base',
                    'o1': 'UAV',
                }  
            posString = "    state.pos = " + str(posDict) + "\n"
    file.write(posString)
    file.write(loadString)
    
    if weather == 'normal':
        file.write("    state.storm = {'active': False}\n")
    elif weather == 'stormy':
        file.write("    state.storm = {'active': True}\n")

    file.write("\ntasks = {\n")

    if numTasks == 1:
        time1 = random.randint(1, 8)
        time_event = time1 + 2
        taskString1 = "    {}: [['doActivities', 'UAV', [['{}', '{}'], ['{}', '{}'], ['{}', '{}']]]],\n".format(time1, 
            jobs1[0], jobs1Locs[0], 
            jobs1[1], jobs1Locs[1],
            jobs1[2], jobs1Locs[2])

        file.write(taskString1)

    elif numTasks == 2:

        time1 = random.randint(1, 8)
        time2 = time1 + 2
        time_event = time2 + 1
        taskString1 = "    {}: [['doActivities', 'UAV', [['{}', '{}'], ['{}', '{}']]]],\n".format(time1, 
            jobs1[0], jobs1Locs[0], 
            jobs1[1], jobs1Locs[1])

        file.write(taskString1)

        taskString2 = "    {}: [['doActivities', 'r1', [['{}', '{}'], ['{}', '{}'], ['{}', '{}']]]],\n".format(time2, 
            jobs2[0], jobs2Locs[0], 
            jobs2[1], jobs2Locs[1],
            jobs2[2], jobs2Locs[2])

        file.write(taskString2)
    
    if emergency == True:
        emergencyString = "    {}: [['handleEmergency', 'r2', '{}']],\n".format(time_event, random.choice(map.locations))
        file.write(emergencyString)
        file.write("}\n")
        
        file.write("\neventsEnv = {\n")
        file.write("    {}: [alienSpotted, ['z2']]\n".format(time_event))
        file.write("}")
    else:

        file.write("}\n")
        
        file.write("eventsEnv = {\n")
        file.write("}")

    file.close() 

def writeHeader(file):
    file.write("__author__ = 'patras'\n")
    file.write("from domain_exploreEnv import *\n") 
    file.write("from timer import DURATION\n") 
    file.write("from state import state, rv\n\n") 

    file.write("DURATION.TIME = {\n")
    file.write("    'survey': 5,\n") 
    file.write("    'monitor': 5,\n") 
    file.write("    'screen': 5,\n") 
    file.write("    'sample': 5,\n") 
    file.write("    'process': 5,\n") 
    file.write("    'fly': 3,\n") 
    file.write("    'deposit': 1,\n") 
    file.write("    'transferData': 1,\n") 
    file.write("    'take': 2,\n") 
    file.write("    'put': 2,\n") 
    file.write("    'move': 10,\n") 
    file.write("    'charge': 5,\n") 
    file.write("    'negotiate': 5,\n") 
    file.write("    'handleAlien': 5,\n") 
    file.write("}\n\n") 

    file.write("DURATION.COUNTER = {\n") 
    file.write("    'survey': 5,\n") 
    file.write("    'monitor': 5,\n") 
    file.write("    'screen': 5,\n") 
    file.write("    'sample': 5,\n") 
    file.write("    'process': 5,\n") 
    file.write("    'fly': 3,\n") 
    file.write("    'deposit': 1,\n") 
    file.write("    'transferData': 1,\n") 
    file.write("    'take': 2,\n") 
    file.write("    'put': 2,\n") 
    file.write("    'move': 10,\n") 
    file.write("    'charge': 5,\n") 
    file.write("    'negotiate': 5,\n") 
    file.write("    'handleAlien': 5,\n") 
    file.write("}\n\n") 

if __name__=="__main__":
    generateProblems()