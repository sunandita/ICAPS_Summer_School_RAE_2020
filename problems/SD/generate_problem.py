import random
import math

def generateProblems():
    num = 1
    for i in range(100):
        writeProblem(num)
        num += 1

adjacentCellsMap = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [2, 4, 6 ,8], 6: [3, 5, 9], 7: [4, 8], 8: [5, 7, 9], 9: [6, 8]}

def adjacentCells(cells):
    adjacentCells = set()
    for cell in cells:
        adjacentCells.update(adjacentCellsMap[cell])
    return adjacentCells - set(cells)

def addEdge(edges, a, b):
    if a in edges:
        if b not in edges[a]:
            edges[a].append(b)
    else:
        edges[a] = [b]
    if b in edges:
        if a not in edges[b]:
            edges[b].append(a)
    else:
        edges[b] = [a]

def backTrackEdge(newCell, cells):
    return [cell for cell in adjacentCellsMap[newCell] if cell in cells]

def uniqueRandomChoices(data, k):
    ret = []
    while k > 0 and data:
        elem = random.choice(data) 
        data.remove(elem) 
        ret.append(elem)
        k -= 1
    return ret

def writeProblem(num):
    fname = 'auto/problem{}_SD.py'.format(num)
    file = open(fname,"w") 
    writeHeader(file)

    numLocations = random.randint(3,8)

    cells = [1]
    cellToNum = {1: 1}
    edges = {}
    for i in range(1, numLocations):
        # print(i,":")
        newCell = random.choice(list(adjacentCells(cells)))
        # print("newCell :",newCell)
        cellToNum[newCell] = i + 1
        # print(cellToNum)
        backEdges = [cell for cell in adjacentCellsMap[newCell] if cell in cells]
        for backEdge in random.choices(backEdges, k = random.randint(1, len(backEdges))):
            addEdge(edges, cellToNum[backEdge], cellToNum[newCell])
        cells.append(newCell)
        # print(edges)

    uniqueEdges = set()
    for a in edges:
        for b in edges[a]:
            if (a, b) not in uniqueEdges and (b, a) not in uniqueEdges:
                uniqueEdges.add((a,b))

    # print("uniqueEdges",uniqueEdges)

    numDoors = random.randint(1, len(uniqueEdges))
    doorLocations = {}
    doors = []
    uniqueRandomEdges = uniqueRandomChoices(list(uniqueEdges), k = numDoors)
    for i in range(len(uniqueRandomEdges)):
        doorName = "d" + str(i+1)
        doors.append(doorName)
        doorLocations[uniqueRandomEdges[i]] = doorName

    numRobots = random.choice([2,2,3]) if numLocations < 5 else random.choice([2,3])
    robots = ["r" + str(i + 1) for i in range(numRobots)]
    objects = ["o" + str(i + 1) for i in range(numRobots)]
    locations = [i + 1 for i in range(numLocations)]

    doorTypes = {}
    stateDoorStatus = {}
    stateLoc = {}
    statePos = {}
    for door in doors:
        doorTypes[door] = random.choice(['spring', 'ordinary'])
        stateDoorStatus[door] = 'closed'
    for robot in robots:
        stateLoc[robot] = random.choice(locations)
    for obj in objects:
        statePos[obj] = random.choice(locations)

    # rv.LOCATIONS = [1, 2, 3, 4, 5, 6]
    file.write("rv.LOCATIONS = ")
    file.write(str(locations))
    file.write("\n")
    # rv.EDGES = {1: [4], 2: [5], 3: [6], 4: [1, 5], 5: [2, 4, 6], 6: [3, 5]}
    file.write("rv.EDGES = ")
    file.write(str(edges))
    file.write("\n")
    # rv.DOORLOCATIONS = {(1, 4): 'd1', (2, 5): 'd2', (3, 6): 'd3'}
    file.write("rv.DOORLOCATIONS = ")
    file.write(str(doorLocations))
    file.write("\n")
    # rv.ROBOTS = ['r1', 'r2']
    file.write("rv.ROBOTS = ")
    file.write(str(robots))
    file.write("\n")
    # rv.DOORS = ['d1', 'd2', 'd3']
    file.write("rv.DOORS = ")
    file.write(str(doors))
    file.write("\n")
    # rv.DOORTYPES = { 'd1': 'spring', 'd2': 'spring', 'd3': 'spring'}
    file.write("rv.DOORTYPES = ")
    file.write(str(doorTypes))
    file.write("\n\n")

    file.write("def ResetState():\n")
    # state.load = {'r1': NIL, 'r2': NIL}
    file.write("    state.load = {" + ', '.join(['\'{}\': NIL'.format(robot) for robot in robots]))
    file.write("}\n")
    # state.doorStatus = {'d1': 'closed', 'd2': 'closed', 'd3': 'closed' }
    file.write("    state.doorStatus = ")
    file.write(str(stateDoorStatus))
    file.write("\n")
    # state.loc = {'r1': 6, 'r2': 5}
    file.write("    state.loc = ")
    file.write(str(stateLoc))
    file.write("\n")
    # state.pos = {'o1': 3}
    file.write("    state.pos = ")
    file.write(str(statePos))
    file.write("\n")
    # state.doorType = {'d1': UNK, 'd2': UNK, 'd3': UNK }
    file.write("    state.doorType = {" + ', '.join(['\'{}\': UNK'.format(door) for door in doors]))
    file.write("}\n\n")

    file.write("tasks = {\n")
    # 5: [['fetch', 'r1', 'o1', 2]]
    #    5: [['moveTo', 'r2', 1]],
    tasks = []
    for i in range(random.choice([1,1,1,2,2,3])):
        task = random.choice(['fetch','moveTo'])
        if task == 'fetch':
            tasks.append('{}: [[\'fetch\', \'{}\', \'{}\', {}]]'.format(random.randint(1,5), random.choice(robots), random.choice(objects), random.choice(locations)))
        else:
            tasks.append('{}: [[\'moveTo\', \'{}\', {}]]'.format(random.randint(1,5), random.choice(robots), random.choice(locations)))
            
    file.write("    " + ',\n    '.join(tasks) + "\n")
    file.write("}\n\n")

    file.write("eventsEnv = {")
    file.write("}\n\n")

    file.close() 
    
def checkEdges(edges):
    for c1 in edges:
        for c2 in edges[c1]:
            if c1 not in edges[c2]:
                return False
    return True

def writeHeader(file):
    file.write("__author__ = 'patras'\n\n")
    file.write("from domain_springDoor import *\n") 
    file.write("from timer import DURATION\n") 
    file.write("from state import state\n\n") 

    file.write("DURATION.TIME = {\n")
    file.write("    'unlatch1': 5,\n")
    file.write("    'unlatch2': 5,\n")
    file.write("    'holdDoor': 2,\n")
    file.write("    'passDoor': 3,\n")
    file.write("    'releaseDoor': 2,\n")
    file.write("    'closeDoors': 3,\n")
    file.write("    'move': 10,\n")
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
    file.write("    'move': 10,\n")
    file.write("    'take': 2,\n")
    file.write("    'put': 2,\n")
    file.write("}\n\n")

if __name__=="__main__":
    generateProblems()