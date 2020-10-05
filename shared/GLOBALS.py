__author__ = 'patras'

class G():
    def __init__(self):
        pass

class RaeArgs():
    def __init__(self):
        pass

g = G()
g.planner = None
g.planningMode = False
g.heuristic = None
g.backupUCT = False

def SetPlanner(p):
    if p == "UPOM":
        g.planner = "UPOM"
    elif p == "RAEPlan":
        g.planner = "RAEPlan"
    else:
        g.planner = None

def GetPlanner():
    return g.planner

def SetPlanningMode(s):
    g.planningMode = s

def GetPlanningMode():
    return g.planningMode

def GetShowOutputs():
    return g.showOutputs

def SetShowOutputs(o):
    g.showOutputs = o

def Setb(b): # number of methods to look at for every task/sub-task
    g.b = b

def Getb():
    return g.b

def Getk(): # number of outputs of commands to look at
    return g.k

def Setk(k):
    g.k = k

def SetMaxDepth(d):
    g.depth = d

def GetMaxDepth():
    return g.depth

def SetHeuristicName(name):
    g.heuristic = name

def GetHeuristicName():
    return g.heuristic

def GetUtility():
    return g.opt 

def SetUtility(opt):
    assert(opt == 'efficiency' or opt == 'successRatio' or opt == "resilience")
    g.opt = opt

def Set_nRO(v):
    g.nro = v

def Get_nRO():
    return g.nro

def GetC():
    return 2

def SetDomain(dom):
    g.domain = dom

def GetDomain():
    return g.domain

def SetTimeLimit(t):
    g.timeLimit = t

def GetTimeLimit():
    return g.timeLimit

def SetDataGenerationMode(a):
    g.dataGenMode = a

def GetDataGenerationMode():
    return g.dataGenMode

def SetUseTrainedModel(t):
    if t == 'None':
        t = None
    g.useTrainedModel = t

def GetUseTrainedModel():
    return g.useTrainedModel

def SetModelPath(p):
    g.modelPath = p

def GetModelPath():
    return g.modelPath

def SetBackupUCT(b):
    g.backupUCT = b

def GetBackupUCT():
    return g.backupUCT

def SetDoIterativeDeepening(s):
    g.iterativeDeepening = s

def GetDoIterativeDeepening():
    return g.iterativeDeepening