import random
import math

class Map():
    def __init__(self, initIndex):
        if initIndex == 1:
            self.locations = [1, 2, 3, 4]
            self.edges = {
                1: [2], 
                2: [1, 3], 
                3: [2, 4], 
                4: [3]
            }
            self.doors = ['d1', 'd2']
            self.doorLocations = {
                (3,4): 'd1',
                (1,2): 'd2',
            }
            self.paths = [(2,4), (2,1), (4, 1), (1,2)]
            self.doorTypes = {
                'd1': random.choice(['spring', 'ordinary']),
                'd2': 'spring',
            }

        elif initIndex == 2:
            self.locations = [1, 2, 3, 4, 5, 6]
            self.edges = {
                1: [4], 
                2: [5], 
                3: [6], 
                4: [1, 5], 
                5: [2, 4, 6], 
                6: [3, 5]
            }
            self.doors = ['d1', 'd2', 'd3']
            self.doorLocations = {
                (1,4): 'd3',
                (2,5): 'd2',
                (3,6): 'd1',
            }
            self.paths = [(1,3), (1,2), (4, 3), (4,2)]
            self.doorTypes = {
                'd1': random.choice(['spring', 'ordinary']),
                'd2': 'spring',
                'd3': 'spring',
            }

        elif initIndex == 3:
            self.locations = [1, 2, 3, 4, 5]
            self.edges = {
                1: [2],
                2: [1, 3],
                3: [2, 4, 5],
                4: [3],
                5: [3]
            }
            self.doors = ['d1', 'd2']
            self.doorLocations = {
                (2,3): 'd1',
                (3,5): 'd2',
            }
            self.doorTypes = {
                'd1': random.choice(['spring', 'ordinary']),
                'd2': 'spring',
            }

            self.paths = [(1,3), (1,2), (4,3), (4,2)]

        elif initIndex == 4:
            self.locations = [1, 2, 3, 4, 5, 6, 7]
            self.edges = {
                1: [7],
                2: [6, 7],
                3: [7],
                4: [5],
                5: [4, 6, 7],
                6: [2, 5],
                7: [1, 2, 3, 5]
            }
            self.doors = ['d1', 'd2', 'd3']
            self.doorLocations = {
                (1,7): 'd1',
                (2,7): 'd2',
                (5,6): 'd3',
            }
            self.doorTypes = {
                'd1': random.choice(['spring', 'ordinary']),
                'd2': 'spring',
                'd3': 'spring',
            }

            self.paths = [(1,6), (1,4), (1,2), (2,4)]

    def GetLocationsString(self):
        return "rv.LOCATIONS = " + str(self.locations) + "\n"

    def GetEdgesString(self):
        return "rv.EDGES = " + str(self.edges) + "\n"

    def GetDoorsString(self):
        return "rv.DOORS = " + str(self.doors) + "\n"

    def GetDoorLocationString(self):
        return "rv.DOORLOCATIONS = " + str(self.doorLocations) + "\n"

    def GetRandomLoc(self):
        return random.choice(self.locations)

    def SelectObjLocs(self, path):
        (l1, l2) = path
        l = self.locations.copy()
        l.remove(l1)
        l.remove(l2)
        random.shuffle(l)
        print("locs = ", self.locations)
        print("l = ", l)
        return [l[0], l[1]]

    def GetDoorTypeString(self):
        return "rv.DOORTYPES = " + str(self.doorTypes) + "\n"
 
    def GetDoorTypeStateString(self):
        res = "    state.doorType = {"
        for d in self.doors:
            res += "'{}': UNK, ".format(d)
        res += "}\n"
        return res

    def GetDoorStatusString(self):
        res = "    state.doorStatus = {"
        for d in self.doors:
            res += "'{}': 'closed', ".format(d)
        res += "}\n"
        return res

def generateProblems():
    num = 1
    for map in [Map(1), Map(2), Map(3), Map(4)]:
        for path in map.paths:  
            objLocs = map.SelectObjLocs(path)
            for l in objLocs:
                for robotCount in [3,4]:
                    for collision in [True, False]:
                        writeProblem(num, map, path, l, robotCount, collision)
                        num += 1

def writeProblem(num, map, path, objLoc, robotCount, collision):
    fname = 'auto/problem{}_SD.py'.format(num)
    file = open(fname,"w") 
    writeHeader(file)

    file.write(map.GetLocationsString()) # LOCATIONS
    file.write(map.GetEdgesString()) # EDGES
    file.write(map.GetDoorsString()) # DOORS
    file.write(map.GetDoorLocationString()) # DOORLOCATIONS
    file.write(map.GetDoorTypeString()) # DOORTYPES

    (l1, l_final) = path
    l2 = map.GetRandomLoc()
    l3 = map.GetRandomLoc()
    l4 = map.GetRandomLoc()
    if robotCount == 3:
        file.write("rv.ROBOTS = ['r1', 'r2', 'r3']\n\n")
        file.write("def ResetState():\n")
        file.write("    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL}\n")
        file.write("    state.status = {'r1': 'free', 'r2': 'free', 'r3': 'free'}\n")
        file.write("    state.loc = {{'r1': {}, 'r2': {}, 'r3': {}}}\n".format(l1, l2, l3))
    else:
        file.write("rv.ROBOTS = ['r1', 'r2', 'r3', 'r4']\n\n")
        file.write("def ResetState():\n")
        file.write("    state.load = {'r1': NIL, 'r2': NIL, 'r3': NIL, 'r4': NIL}\n")
        file.write("    state.status = {'r1': 'free', 'r2': 'free', 'r3': 'free', 'r4': 'free'}\n")
        file.write("    state.loc = {{'r1': {}, 'r2': {}, 'r3': {}, 'r4': {}}}\n".format(l1, l2, l3, l4))

    file.write("    state.pos = {{'o1': {}}}\n".format(map.GetRandomLoc()))
    file.write(map.GetDoorStatusString())
    file.write(map.GetDoorTypeStateString())

    file.write("\ntasks = {\n")
    t1 = random.randint(1, 10)
    t2 = t1 + random.randint(1,5)

    taskString = "    {}: [['fetch', 'r1', 'o1', {}]],\n".format(t1, l_final)
    file.write(taskString)
    
    if collision == True:
        file.write("    {}: [['collision', 'r1']],\n".format(t2))
    file.write("}\n")

    file.write("eventsEnv = {\n")
    file.write("}")


    file.close() 
    
def writeHeader(file):
    file.write("__author__ = 'patras'\n\n")
    file.write("from domain_springDoor import *\n") 
    file.write("from timer import DURATION\n") 
    file.write("from state import state, rv\n\n") 

    file.write("DURATION.TIME = {\n")
    file.write("    'unlatch1': 5,\n")
    file.write("    'unlatch2': 5,\n")
    file.write("    'holdDoor': 2,\n")
    file.write("    'passDoor': 3,\n")
    file.write("    'releaseDoor': 2,\n")
    file.write("    'closeDoors': 3,\n")
    file.write("    'move': 7,\n")
    file.write("    'take': 2,\n")
    file.write("    'put': 2,\n")
    file.write("}\n\n")

    file.write("DURATION.COUNTER = {\n")
    file.write("    'unlatch1': 5,\n")
    file.write("    'unlatch2': 5,\n")
    file.write("    'holdDoor': 2,\n")
    file.write("    'passDoor': 3,\n")
    file.write("    'releaseDoor': 2,\n")
    file.write("    'closeDoors': 3,\n")
    file.write("    'move': 7,\n")
    file.write("    'take': 2,\n")
    file.write("    'put': 2,\n")
    file.write("}\n\n")

if __name__=="__main__":
    generateProblems()