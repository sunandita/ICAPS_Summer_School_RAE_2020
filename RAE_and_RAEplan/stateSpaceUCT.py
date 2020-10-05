__author__="__patras__"

import multiprocessing
from state import RestoreState, GetState
import GLOBALS
from utility import Utility
from dataStructures import rL_PLAN
import random
from timer import DURATION
import types
import math

goalChecks = {}
commands = {}
planLocals = rL_PLAN()

class ssuNode():
    def __init__(self, l, t, args):
        self.label = l
        self.args = args
        assert(t == "command" or t == "state")
        self.type = t
        self.children = []
        self.childPtr = 0
        self.childWeights = []
        self.util = Utility("UNK")
        self.parent = None
        assert(GLOBALS.GetUCTmode() == True)
        if self.type == 'state':
            self.N = 0
            self.n = []
            self.Q = []

    def GetLabel(self):
        return self.label

    def GetType(self):
        return self.type

    def SetUtility(self, u):
        self.util = u

    def GetUtility(self):
        return self.util

    def SetParent(self, p):
        self.parent = p

    def GetParent(self):
        return self.parent

    def AddChild(self, node):
        node.parent = self
        self.children.append(node)
        self.childWeights.append(1)
        if self.type == 'state':
            self.n.append(0)
            self.Q.append(Utility('Success'))

    def FindAmongChildren(self, s):
        assert(self.type == 'command')
        for child in self.children:
            if child.label.EqualTo(s):
                return child 
        return None

    def GetNext(self):
        if self.childPtr < len(self.children):
            return self.children[self.childPtr]
        else:
            return None

    def GetBestCommand(self):
        index = None
        bestQ = Utility('Failure')
        
        #l = [q.GetValue() for q in self.Q]
        for i in range(0, len(self.Q)):
            if self.Q[i] > bestQ:
                bestQ = self.Q[i]
                index = i
        if index == None:
            return 'Failure'
        else:
            return self.children[index].GetLabel()
        
    def IncreaseWeight(self, s):
        assert(self.type == 'command')
        for index in range(0, len(self.children)):
            if self.children[index].GetLabel().EqualTo(s):
                self.childWeights[index] += 1

    def GetPrettyString(self, elem):
        if elem.type == 'command':
            return elem.label.__name__
        elif elem.type == 'state':
            return "state"
        else:
            return "NONE"

    def PrintUsingGraphviz(self, name='searchTreeWithCommandsOnly'):
        g = Digraph('G', filename=name, format="png")

        level = {}
        level[0] = [(self, 0)] # tuple of node and node id
        level[1] = []
        curr = 0
        next = 1
        newId = 1
        while(level[curr] != []):
            for elem, nodeid in level[curr]:
                elemString = self.GetPrettyString(elem) + "_" + str(nodeid)
                for child in elem.children:
                    g.edge(elemString, self.GetPrettyString(child) + "_" + str(newId))
                    level[next].append((child, newId))
                    newId += 1
            curr += 1
            next += 1
            level[next] = []
        g.view()

class PlanM():
    def __init__(self, p):
        self.plan = p
        print("State Space UCT has come up with:")
        print(self.plan)
        exit(1)

    def Call(self):
        for item in self.plan:
            print("Doing ", item.__name__)
            RAE1_and_RAEplan.do_command(item)

def declare_commands(cmd_list):
    commands.update({cmd.__name__:cmd for cmd in cmd_list})

def declare_goalCheck(task, goalCheckMethod):
    goalChecks[task] = goalCheckMethod

def StateSpaceUCT(task, taskArgs, initState, queue):

    root = ssuNode(initState.copy() , 'state', None)

    for i in range(GLOBALS.GetUCTRuns()):
        RestoreState(root.GetLabel())
        planLocals.SetSearchTreeNode(root)
        planLocals.SetUtilRollout(Utility("Success"))
        DoOneRollout(task, taskArgs)

    sNode = root
    plan = []
    bestQ = Utility('Failure')
    bestC = "Failure"
    while(sNode.children != []):

        for i in range(0, len(sNode.Q)):
            if sNode.n[i] > 0:
                if sNode.Q[i] > bestQ: 
                    bestQ = sNode.Q[i]
                    bestC = sNode.children[i]
        if bestC == "Failure":
            queue.put("Failure")
            return
        plan.append(bestC.GetLabel())
        bestW = 0
        for i in range(0, len(bestC.children)):
            if bestC.childWeights[i] > bestW:
                bestW = bestC.childWeights[i]
                sNode = bestC.children[i]

    queue.put(PlanM(plan))

def StateSpaceUCTMain(task, taskArgs):

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(
            target=StateSpaceUCT,
            args=[task, taskArgs, GetState(), queue])

    p.start()
    p.join(int(0.7*GLOBALS.GetTimeLimit())) # planner gets max 70% of the total time

    if p.is_alive() == True:
        p.terminate()
        return 'Failure'
    else:
        plan = queue.get()
        return plan

def DoOneRollout(task, taskArgs):
    goalCheck = goalChecks[task]
    if goalCheck(*taskArgs) == True:
        return

    curNode = planLocals.GetSearchTreeNode()
    if curNode.children == []:
        for cmd in commands.values():
            newSearchTreeNode = ssuNode(cmd, 'command', [])
            curNode.AddChild(newSearchTreeNode)

    untried = []

    if curNode.N == 0:
        untried = curNode.children
    else:
        for child in curNode.children:
            if child.children == []:
                untried.append(child) # command that has not been simulated yet

    if untried != []:
        cNode = random.choice(untried)
        index = curNode.children.index(cNode)
    else:
        vmax = 0
        cNode = None
        index = None
        for i in range(0, len(curNode.children)):
            v = curNode.Q[i].GetValue() + \
                GLOBALS.GetC() * math.sqrt(math.log(curNode.N)/curNode.n[i])
            if v >= vmax:
                vmax = v
                cNode = curNode.children[i]
                index = i

    c = cNode.GetLabel()
    cmdRet = {'state':'running'}
    RAE1_and_RAEplan.beginCommand(c, cmdRet, [])
    retcode = cmdRet['state']

    nextState = GetState().copy()

    if retcode == 'Failure':
        nSN = ssuNode(nextState, 'state', None) # next state node
        nSN.SetUtility(Utility('Failure'))
        cNode.AddChild(nSN)
        planLocals.SetUtilRollout(Utility('Failure'))
        curNode.Q[index] = Utility('Failure')
    else:
        nSN = cNode.FindAmongChildren(nextState) 
        if nSN == None:
            nSN = ssuNode(nextState, 'state', None)
            cNode.AddChild(nSN)
        else:
            cNode.IncreaseWeight(nextState)
        
        util1 = planLocals.GetUtilRollout()
        util2 = RAE1_and_RAEplan.GetUtility(c, []) # cmdArgs
        planLocals.SetUtilRollout(util1 + util2)
        nSN.SetUtility(RAE1_and_RAEplan.GetUtility(c, [])) # cmdArgs
        planLocals.SetSearchTreeNode(nSN)

        DoOneRollout(task, taskArgs)

        utilVal = planLocals.GetUtilRollout().GetValue()
        if curNode.n[index] > 0:
            curNode.Q[index] = Utility((curNode.Q[index].GetValue() * \
                                curNode.n[index] + \
                                utilVal) / \
                            (curNode.n[index] + 1))
        else:
            curNode.Q[index] = Utility(utilVal)

    curNode.n[index] += 1
    curNode.N += 1

import RAE1_and_RAEplan
