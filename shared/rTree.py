__author__ = 'patras'

import pipes
from timer import DURATION
#from graphviz import Digraph
import types
from utility import Utility
import GLOBALS
from learningData import TrainingDataItem
import pdb

rollOuts = 0
class PlanningTree():
    def __init__(self, n, args, type1):
        self.label = n # name of the method or task corresponding to this node
        self.args = args # arguments of the method corresponding to this node
        self.type = type1 # whether this is a task or a method or command
        
        self.children = [] # list of children of this node

        # only for RAEplan
        self.util = Utility('Success') # efficiency of this node

        # only for APEplan 
        self.state = None # state needs to be set after planning for sub-tasks

    def GetState(self):
        return self.state

    def SetState(self, s):
        self.state = s

    def GetLabel(self):
        return self.label

    def GetArgs(self):
        return self.args

    def GetRetcode(self):
        if self.label == "Failure":
            return "Failure"
        else:
            return "Success"

    def GetPreorderTraversal(self):
        if self.label == None:
            return []
        else:
            res = [self.label]
            for node in self.children:
                res = res + node.GetPreorderTraversal()
            return res

    def AddUtility(self, u2):
        self.util = self.util + u2

    def GetUtility(self):
        return self.util

    def GetMethod(self):
        if self.type == 'method':
            return self.label
        else:
            print("ERR MSG: Type mistach in Refinement Tree")
            print("ERR MSG: Asking for method when the type is ", self.type)
            return None

    def DeleteAllChildren(self):
        assert(self.label == "root")
        self.children = []
        self.SetUtility(Utility('Success'))

    def GetChild(self):
        assert(len(self.children) == 1)
        return self.children[0]

    def AddChild(self, node):
        self.children = self.children + [node]

    def SetUtility(self, u):
        self.util = u

    def GetPrettyString(self):
        if self.label == 'root' or self.label == 'Failure':
            return self.label
        if self.label != None:
            return self.label.__name__
        else:
            return "NONE"

    def GetInEtcFormat(self):
        if self.children == []:
            return self.GetPrettyString()
        else:
            res = "(" + ",".join(elem.GetInEtcFormat() for elem in self.children)
            res += ")" + self.GetPrettyString()            
        return res

    def PrintUsingPipeline(self):
        treeString = self.GetInEtcFormat() + ";"
        #print(treeString)
        t = pipes.Template()
        f = t.open('pipefile', 'w')
        f.write(treeString)
        f.close()

    def PrintUsingGraphviz(self, name='visual'):
        g = Digraph('G', filename=name, format="png")

        level = {}
        level[0] = [(self, 0)] # tuple of node and node id
        level[1] = []
        curr = 0
        next = 1
        newId = 1
        while(level[curr] != []):
            for elem, nodeid in level[curr]:
                elemString = elem.GetPrettyString() + "_" + str(nodeid)
                for child in elem.children:
                    g.edge(elemString, child.GetPrettyString() + "_" + str(newId))
                    level[next].append((child, newId))
                    newId += 1
            curr += 1
            next += 1
            level[next] = []
        g.view()

    def PrintInTerminal(self):
        level = {}
        level[0] = [self]
        level[1] = []
        curr = 0
        next = 1
        print("\n------PLANNING TREE-------")
        print("UTILITY = ", self.GetUtility())
        while(level[curr] != []):
            print(' '.join(elem.GetPrettyString() for elem in level[curr]))
            for elem in level[curr]:
                level[next] += elem.children
            curr += 1
            next += 1
            level[next] = []
        print("\n------------------------")

    def copy(self):
        r = PlanningTree(self.label, self.args, self.type)
        r.SetUtility(self.util)
        if self.children == []:
            return r
        else:
            for child in self.children:
                c_copy = child.copy()
                r.children = r.children + [c_copy]
        return r

    def GetSize(self):
        "returns the number of nodes of the tree with this as root"
        if self.type == 'method' or self.label == 'root':
            count = 1
            for c in self.children:
                count += c.GetSize()
            return count
        else:
            return 0 # Don't want to count the commands

    def GetNumberOfCommands(self):
        "returns the number of commands of this tree"
        if self.type == 'method' or self.label == 'root':
            count = 0
            for c in self.children:
                count += c.GetSize()
            return count
        else:
            return 1 # Count the commands

def CreateFailureNode():
    tnode = PlanningTree('Failure', 'Failure', 'Failure')
    tnode.SetUtility(Utility('Failure'))
    return tnode

class ActingNode():
    def __init__(self, m):
        self.label = m
        self.type = 'method'
        self.children = []
        self.parent = None
        self.nextState = None
        self.prevState = None

    def SetLabelAndType(self, l, ty, cmdArgs=None):
        self.label = l
        assert(ty == 'method' or ty == 'command')
        self.type = ty
        if ty == 'command':
            assert(cmdArgs != None)
            self.cmdArgs = cmdArgs

    def GetType(self):
        return self.type

    def GetLabel(self):
        return self.label

    def Clear(self):
        self.children = []
        self.label = None

    def AddChild(self):
        newNode = ActingNode(None)
        newNode.parent = self
        self.children.append(newNode)
        return newNode

    def GetPrettyString(self, elem):
        if elem.label == 'root':
            return 'root'
        if elem.label != None:
            if elem.type == 'method':
                return elem.label.GetName()
            else:
                return elem.label.__name__
        else:
            return "NONE"

    def SetNextState(self, s):
        self.nextState = s

    def GetNextState(self):
        return self.nextState

    def SetPrevState(self, s):
        self.prevState = s

    def GetPrevState(self):
        return self.prevState

    def GetChild(self):
        assert(len(self.children) == 1)
        return self.children[0]

    def Print(self):
        level = {}
        level[0] = [self]
        level[1] = []
        curr = 0
        next = 1

        while(level[curr] != []):
            print(' '.join(self.GetPrettyString(elem) for elem in level[curr]))
            for elem in level[curr]:
                level[next] += elem.children
            curr += 1
            next += 1
            level[next] = []

    def PrintUsingGraphViz(self, name):
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

    def GetSuccessor(self):
        if self.children != []:
            return self.children[0] # the first child of this node
        else:
            # travel upwards in the tree until you find an ancestor with a next child
            parent = self.parent
            curr_child = self
            while(True):
                if parent == None:
                    return None # No possible successor, you have reached the end of the tree
                else:
                    index = parent.children.index(curr_child)
                    if index < len(parent.children) - 1: # found the successor!
                        return parent.children[index + 1]
                curr_child = parent
                parent = parent.parent

    def GetSize(self):
        "returns the number of nodes of the tree with this as root"
        if self.type == 'method':
            count = 1
            for c in self.children:
                count += c.GetSize()
            return count
        else:
            return 1

    def GetPreorderTraversal(self):
        if self.label == None:
            return []
        else:
            res = [self]
            for node in self.children:
                res = res + node.GetPreorderTraversal()
            return res

    def GetCost(self):
        if self.type == 'command':
            assert(self.label.__name__ != "fail")
            cost = DURATION.COUNTER[self.label.__name__]
            if type(cost) == types.FunctionType:
                return cost(*self.cmdArgs)
            else:
                return cost
        else:
            return 0

    def GetMetaData(self):
        if self.type == 'command':
            return 0, 0, 1
        else:
            h = 1
            t = 1
            c = 0
            h_max = 0
            for child in self.children:
                maxHeight, taskCount, commandCount = child.GetMetaData()
                t += taskCount
                c += commandCount
                if maxHeight > h_max:
                    h_max = maxHeight
            h += h_max
            return h, t, c

class ActingTree():
    def __init__(self):
        self.root = ActingNode('root')
        self.currPtr = self.root

    def GetCurrNode(self):
        return self.currPtr

    def SetCurrNode(self, n):
        self.currPtr = n

    def SetNextState(self, s):
        self.currPtr.SetNextState(s)

    def GetNextState(self):
        return self.currPtr.GetNextState()

    def SetPrevState(self, s):
        self.currPtr.SetPrevState(s)

    def GetPrevState(self):
        return self.currPtr.GetPrevState()

    def GetGuideList(self):
        l1 = self.root.GetPreorderTraversal()
        l2 = [GuideNode(elem.GetLabel(), elem.GetPrevState(), elem.GetNextState(), elem.GetCost()) for elem in l1]
        l = GuideList(l2)
        return l

    def GetSearchTree(self):
        l1 = self.root.GetPreorderTraversal()
        root = None
        currNode = None
        for item in l1:
            t = item.GetType()
            if t == "method":
                node = SearchTreeNode('task', 'task', None)
                child = SearchTreeNode(item.GetLabel(), 'method', None)
                child.SetPrevState(item.GetPrevState())
                node.AddChild(child)
            elif t == "command":
                node = SearchTreeNode(item.GetLabel(), 'command', None)
                child = SearchTreeNode(item.GetNextState(), 'state', None)
                child.SetPrevState(item.GetPrevState())
                node.AddChild(child)
            else:
                print("Error: Invalid type.")
            if root == None:
                root = node
            else:
                currNode.AddChild(node)
            currNode = child
        return root

    def GetPreOrderTraversal(self):
        return self.root.GetPreorderTraversal()

    def Print(self):
        print("\n------ACTING TREE-------")
        self.root.Print()
        print("\n------------------------")

    def GetSize(self):
        return self.root.GetSize()

    def PrintUsingGraphviz(self, name='actingTree'):
        self.root.PrintUsingGraphViz(name)

    def GetMetaData(self):
        h, t, c =  self.root.GetMetaData()
        return h - 1, t - 1, c

    def GetLastFiveItems(self):
        preOrder = self.root.GetPreorderTraversal()
        five = [0]*5
        i = 0
        preOrder.reverse()
        for item in preOrder[0:5]:
            five[i] = item.GetPrettyString(item)
            i += 1
        return five

class GuideNode():
    def __init__(self, m, s1, s2, c):
        self.label = m
        self.prevState = s1
        self.nextState = s2
        self.cost = c

    def GetPrettyString(self):
        if self.label == 'root':
            return self.label
        if self.label != None:
            return self.label.__name__
        else:
            return "NONE"

    def SetLabel(self, l):
        self.label = l

    def SetCost(self, c):
        self.cost = c

    def GetNextState(self):
        assert(self.nextState != None)
        return self.nextState

    def SetNextState(self, s):
        self.nextState = s

    def GetPrevState(self):
        assert(self.prevState != None)
        return self.prevState

    def SetPrevState(self, s):
        self.prevState = s

    def GetLabel(self):
        return self.label

    def Print(self):
        print("Label: ", self.label)
        print("Previous State: ", self.prevState)
        print("Next State: ", self.nextState)

    def GetCost(self):
        return self.cost

class GuideList():
    def __init__(self, l):
        self.l = l
        self.currIndex = 1

    def GetNext(self):
        if self.currIndex == len(self.l):
            return None
        else:
            node = self.l[self.currIndex]
            self.currIndex += 1
            return node

    def append(self, m=None, s1=None, s2=None, c=0):
        assert(len(self.l) == self.currIndex)
        n = GuideNode(m, s1, s2, c)
        self.l.append(n)
        return n

    def RemoveAllAfter(self, n):
        if n.GetLabel() != None:
            index = self.l.index(n)
            self.l = self.l[0:index + 1]

    def ResetPtr(self):
        self.currIndex = 1

    def Print(self):
        #print("length = ", len(self.l))
        #return 
        print("\n------GUIDE LIST-------")
        index = 0
        while(index != len(self.l)):
            if index == self.currIndex:
                print(" ----> ")
            self.l[index].Print()
            index += 1
        print("\n------------------------")

    def GetStartState(self):
        return self.l[0].GetPrevState()

    #def GetUtility(self):
    #    cost = 0
    #    for item in self.l:
    #        cost += item.GetCost()

    #    if cost == 0:
    #        return float("inf")
    #    else:
    #        return 1/cost

class SearchTreeNode():
    def __init__(self, l, t, args):
        self.label = l
        self.args = args
        assert(t == "task" or t == "method" or t == "command" or t == "state" or t == "heuristic")
        self.type = t
        self.children = []
        self.childPtr = 0
        self.childWeights = []
        self.util = Utility("UNK")
        self.prevState = None
        self.parent = None
        if GLOBALS.GetPlanner() == "UPOM" and self.type == 'task':
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

    def GetSearchDone(self):
        if self.childPtr == 1:
            return True
        else:
            return False

    def SetParent(self, p):
        self.parent = p

    def GetParent(self):
        return self.parent

    def SetPrevState(self, s):
        self.prevState = s

    def GetPrevState(self):
        return self.prevState

    def AddChild(self, node):
        node.parent = self
        self.children.append(node)
        self.childWeights.append(1)
        if GLOBALS.GetPlanner() == "UPOM" and self.type == 'task':
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

    def IncrementPointerAndSetUtility(self):
        if self.childPtr < len(self.children) - 1:
            self.childPtr += 1
        else:
            if self.type == 'task':
                bestUtil = Utility('Failure')
                for child in self.children:
                    if child.util > bestUtil:
                        bestUtil = child.util
                self.util = bestUtil
            elif self.type == 'command':
                res = 0
                total = 0
                # Take the average of values
                for child, weight in zip(self.children, self.childWeights):
                    res += weight * child.util.GetValue()
                    total += weight
                self.util = Utility(res / total)
            elif self.type == 'state':
                self.util = self.util + self.children[0].util
            else:
                self.util = self.children[0].util

            self.childPtr += 1
            if self.parent != None:
                self.parent.IncrementPointerAndSetUtility()

    def UpdateAllUtilities(self): # for generating training data in UCT
        if self.children == []:
            return self.util  # state nodes at the roots
        elif self.type == "command":
            val = 0
            total = 0
            # Take the average of values
            for child, weight in zip(self.children, self.childWeights):
                val += weight * child.UpdateAllUtilities().GetValue()
                total += weight
            self.util = Utility(val / total)
        elif self.type == "task":
            bestUtil = Utility('Failure')
            for child in self.children:
                cUtil = child.UpdateAllUtilities()
                if cUtil > bestUtil:
                    bestUtil = cUtil
            self.util = bestUtil
        elif self.type == 'state':
            self.util = self.util + self.children[0].UpdateAllUtilities()
        else:
            self.util = self.children[0].UpdateAllUtilities()
        
        return self.util

    def UpdateChildPointers(self): # for SLATE
        if self.children == []:
            global rollOuts
            rollOuts += 1
            #print("Rollout ", rollOuts )
            # reached the bottom of the tree, start moving up now
            self.parent.IncrementPointerAndSetUtility()
        else:
            self.children[self.childPtr].UpdateChildPointers()

    def UpdateQValues(self, utilVal): # for UCT
        if self.type == "task":
            index = self.updateIndex
            if self.n[index] > 0:
                self.Q[index] = \
                    Utility(((utilVal + self.n[index] * self.Q[index].GetValue()) / \
                    (1 + self.n[index])))
            else:
                self.Q[index] = Utility(utilVal)

            self.n[index] += 1
            self.N += 1
            self.updateIndex = None # to be safe
            self.children[index].UpdateQValues(utilVal)
        elif self.type == "method" or self.type == "state":
            if len(self.children) > 0:
                assert(len(self.children) == 1)
                self.children[0].UpdateQValues(utilVal)
        elif self.type == "command":
            child = self.updateChild
            self.updateChild = None
            child.UpdateQValues(utilVal)

    def GetBestMethodAndUtility(self):
        bestMethod = 'Failure'
        bestUtil = Utility('Failure')
        for child in self.children:
            if child.util > bestUtil:
                bestUtil = child.util
                bestMethod = child.GetLabel()
        return (bestMethod, bestUtil)

    def GetBestMethodAndUtility_UPOM(self):
        index = None
        bestQ = Utility('Failure')
        
        #l = [q.GetValue() for q in self.Q]
        for i in range(0, len(self.Q)):
            if self.Q[i] > bestQ:
                bestQ = self.Q[i]
                index = i
        if index == None:
            return ('Failure', bestQ)
        else:
            return (self.children[index].GetLabel(), bestQ)
        
    def IncreaseWeight(self, s):
        assert(self.type == 'command')
        for index in range(0, len(self.children)):
            if self.children[index].GetLabel().EqualTo(s):
                self.childWeights[index] += 1

    def GetPrettyString(self, elem):
        if elem.label == 'task' or elem.type == 'task' or elem.label == 'root' or elem.label == 'heuristic':
            return elem.label
        elif elem.type == 'method':
            return elem.label.GetName()
        elif elem.type == 'command':
            return elem.label.__name__
        elif elem.type == 'state':
            return "state"
        else:
            return "NONE"

    def PrintMethodsAndUtilities(self):
        for i in range(0, len(self.Q)):
            print((self.children[i].GetLabel(), self.Q[i].value))
            
    def PrintUsingGraphviz(self, name='searchTree'):
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

    def GetTrainingItems(self, l, util, mainTask):
        if self.type == "task":
            #for each child get q and labels and add to l
            for i in range(0, len(self.Q)):
                if self.n[i] == 0:
                    pass
                    #print("Found an unexplored path")
                else:
                    if self.children[i].GetLabel() != "heuristic":
                        l.Add(self.children[i].prevState, 
                            self.children[i].GetLabel(), 
                            self.children[i].util, 
                            self.label,
                            self.args, 
                            mainTask, 
                            []) 
                        self.children[i].GetTrainingItems(l, util, mainTask)
        elif self.type == "method" or self.type == "state":
            if len(self.children) > 0:
                self.children[0].GetTrainingItems(l, util, mainTask)
        elif self.type == "command":
            for child in self.children:
                child.GetTrainingItems(l, util, mainTask)

    def GetTrainingItems_SLATE(self, l, util, mainTask):
        if self.type == "task":
            #for each child get q and labels and add to l
            for i in range(0, len(self.children)):
                if self.children[i].label != "heuristic":
                    l.Add(self.children[i].prevState, 
                        self.children[i].GetLabel(), self.children[i].util, 
                        self.label, mainTask, None) 
                    self.children[i].GetTrainingItems_SLATE(l, util, mainTask)
        elif self.type == "method" or self.type == "state":
            if len(self.children) > 0:
                self.children[0].GetTrainingItems_SLATE(l, util, mainTask)
        elif self.type == "command":
            for child in self.children:
                child.GetTrainingItems_SLATE(l, util, mainTask)

