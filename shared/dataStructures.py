__author__ = 'patras'

import threading
import GLOBALS
from utility import *

class rL():
    def __init__(self):
        self.rL = threading.local()

    def SetStackId(self, id):
        self.rL.stackid = id

    def GetStackId(self):
        return self.rL.stackid

class rL_APE(rL):
    def SetMainTask(self, t):
        self.rL.mainTask = t
        self.rL.planningUtilities = []

    def GetMainTask(self):
        return self.rL.mainTask

    def SetMainTaskArgs(self, args):
        self.rL.taskArgs = args

    def GetMainTaskArgs(self):
        return self.rL.taskArgs

    def SetRetryCount(self, count):
        self.rL.rC = count

    def GetRetryCount(self):
        return self.rL.rC

    def SetCommandCount(self, c):
        self.rL.commCount = c

    def GetCommandCount(self):
        return self.rL.commCount

    def SetCurrentNode(self, node):
        self.rL.aT.SetCurrNode(node) 

    def GetCurrentNode(self):
        return self.rL.aT.GetCurrNode()

    def GetCurrentNodes(self):
        aT = self.rL.aT
        parent = aT.GetCurrNode()
        child = parent.AddChild()
        return parent, child

    def SetActingTree(self, aT):
        self.rL.aT = aT

    def GetActingTree(self):
        return self.rL.aT

    def GetGuideList(self):
        l = self.rL.aT.GetGuideList()
        return l

    def SetUtility(self, e):
        self.rL.util = e

    def GetUtility(self):
        return self.rL.util

    def AddToPlanningUtilityList(self, item):
        self.rL.planningUtilities.append(item)

    def GetPlanningUtilitiesList(self):
        return self.rL.planningUtilities

    def SetEfficiency(self, e):
        self.rL.eff = e

    def GetEfficiency(self):
        return self.rL.eff

    def SetUseBackupUCT(self, u):
        self.rL.backupUCT = u

    def GetUseBackupUCT(self):
        return self.rL.backupUCT

class rL_PLAN(rL):

    def __init__(self):
        self.rL = threading.local()

    def GetCandidates(self):
        return self.rL.candidates

    def SetCandidates(self, c):
        self.rL.candidates = c

    def SetState(self, s):
        self.rL.state = s

    def GetState(self):
        return self.rL.state

    def SetCurrentNode(self, n):
        self.rL.currentNode = n

    def GetCurrentNode(self):
        return self.rL.currentNode

    def SetPlanningTree(self, t):
        self.rL.planningTree = t

    def GetPlanningTree(self):
        return self.rL.planningTree

    #def SetGuideList(self, gl):
    #    self.rL.guideList = gl

    #def GetGuideList(self):
    #    return self.rL.guideList

    #def GetBestTree(self):
    #    return self.rL.bestTree 

    #def SetBestTree(self, t):
    #    self.rL.bestTree = t

    def SetSearchTreeNode(self, n):
        self.rL.searchTree = n

    def GetSearchTreeNode(self):
        return self.rL.searchTree

    def GetSearchTreeRoot(self):
        return self.rL.searchTreeRoot

    def SetSearchTreeRoot(self, r):
        self.rL.searchTreeRoot = r

    def SetTaskToRefine(self, taskNode):
        self.rL.taskToRefine = taskNode

    def GetTaskToRefine(self):
        return self.rL.taskToRefine

    def SetFlip(self, v):
        self.rL.flip = v

    def GetFlip(self):
        return self.rL.flip

    def SetDepth(self, d):
        self.rL.depth = d

    def GetDepth(self):
        return self.rL.depth

    def IncreaseDepthBy1(self):
        self.rL.depth += 1

    def SetRefDepth(self, d):
        self.rL.refDepth = d

    def GetRefDepth(self):
        return self.rL.refDepth

    def SetRolloutDepth(self, d):
        self.rL.rolloutDepth = d

    def GetRolloutDepth(self):
        return self.rL.rolloutDepth

    def SetHeuristicArgs(self, t, args):
        self.rL.heuristicTaskName = t
        self.rL.heuristicTaskArgs = args

    def GetHeuristicArgs(self):
        return (self.rL.heuristicTaskName, self.rL.heuristicTaskArgs)

    def SetUtilRollout(self, u):
        self.rL.util = u

    def GetUtilRollout(self):
        return self.rL.util


class PlanArgs():
    def __init__(self):
        pass

    def SetTask(self, t):
        self.task = t
    
    def GetTask(self):
        return self.task

    def GetTaskArgs(self):
        return self.taskArgs

    def SetTaskArgs(self, args):
        self.taskArgs = args

    def SetCandidates(self, cand):
        self.candidates = cand

    def GetCandidates(self):
        return self.candidates

    def SetGuideList(self, t):
        self.actingTree = t

    def GetGuideList(self):
        return self.actingTree

    def GetStackId(self):
        return self.stackid

    def SetStackId(self, id):
        self.stackid = id

    def SetState(self, s):
        self.state = s

    def GetState(self):
        return self.state

    def SetActingTree(self, t):
        self.actingTree = t

    def GetSearchTree(self):
        return self.actingTree.GetSearchTree()

    def SetCurUtil(self, u):
        self.util = u

    def GetCurUtil(self):
        return self.util

    def SetDepth(self, d):
        self.d = d

    def GetDepth(self):
        return self.d
