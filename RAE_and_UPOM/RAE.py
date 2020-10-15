from __future__ import print_function
from RAE1_and_UPOM import ipcArgs, envArgs, RAE1, RAEplan_Choice, UPOM_Choice, GetBestTillNow
from dataStructures import PlanArgs
from timer import globalTimer, SetMode
from state import ReinitializeState, RemoveLocksFromState, RestoreState
import threading
import GLOBALS
import os
import signal
import sys

__author__ = 'patras'

problem_module = None

def GetNextAlive(lastActiveStack, numstacks, threadList):
    '''
    :param lastActiveStack: the stack which was progressed before this
    :param numstacks: total number of stacks in the Agenda
    :param threadList: list of all the threads, each running a RAE stack
    :return: The stack which should be executed next
    '''
    nextAlive = -1
    i = 1
    j = lastActiveStack % numstacks + 1
    while i <= numstacks:
        if threadList[j-1].isAlive() == True:
            nextAlive = j
            break
        i = i + 1
        j = j % numstacks + 1

    return nextAlive

def noNewTasks():
    if GLOBALS.GetDomain() == 'SDN_dev':
        return False
    for c in problem_module.tasks:
        if c > GetNewTasks.counter:
            return False
    return True

def GetNewTasks():
    '''
    :return: gets the new task that appears in the problem at the current time
    '''
    GetNewTasks.counter += 1
    if GLOBALS.GetDomain() != 'SDN_dev':
        if GetNewTasks.counter in problem_module.tasks:
            return problem_module.tasks[GetNewTasks.counter]
        else:
            return []
    else:
        tasks = []
        while not taskQueue.empty():
            tasks.append(taskQueue.get())
        return tasks

def InitializeDomain(domain, problem, startState=None):
    '''
    :param domain: code of the domain which you are running
    :param problem: id of the problem
    :return:none
    '''
    if domain in ['CR', 'SD', 'EE', 'SR', 'OF', 'test']:
        module = problem + '_' + domain
        global problem_module
        ReinitializeState()    # useful for batch runs to start with the starting state
        problem_module = __import__(module)
        problem_module.ResetState()
        return problem_module
    else:
        print("Invalid domain\n", domain)
        exit(11)

def BeginFreshIteration(lastActiveStack, numstacks, threadList):
    begin = True
    i = lastActiveStack % numstacks + 1
    while i != 1:
        if threadList[i - 1].isAlive() == True:
            begin = False
            break
        i = i % numstacks + 1
    return begin

def CreateNewStack(taskInfo, raeArgs):
    stackid = raeArgs.stack
    retcode, retryCount, eff, height, taskCount, commandCount, utilVal, utilitiesList = RAE1(raeArgs.task, raeArgs)
    taskInfo[stackid] = ([raeArgs.task] + raeArgs.taskArgs, retcode, retryCount, eff, height, taskCount, commandCount, utilVal, utilitiesList)

def PrintResult(taskInfo):
    print("RESULTS:")
    for stackid in taskInfo:
        args, res, retryCount, eff, height, taskCount, commandCount, utilVal, utilitiesList = taskInfo[stackid]
        
        print(
            '\n Task : ', '\t{}{}'.format(args[0], args[1:]),
            '\n Result : \t', res,
            '\n Retry Count: \t', retryCount, 
            '\n Efficiency: \t', eff, 
            )
        print("-----------------")

def PrintResultSummaryVersion1(taskInfo):
    succ = 0
    fail = 0
    retries = 0
    effTotal = 0
    h = 0
    t = 0
    c = 0
    for stackid in taskInfo:
        args, res, retryCount, eff, height, taskCount, commandCount = taskInfo[stackid]
        if res == 'Success':
            succ += 1
        else:
            fail += 1
        retries += retryCount
        effTotal += eff.GetValue()
        c += commandCount
        t += taskCount
        if height > h:
            h = height
    print(succ, succ+fail, retries, globalTimer.GetSimulationCounter(), globalTimer.GetRealCommandExecutionCounter(), effTotal, h, t, c)
    #print(' '.join('-'.join([key, str(cmdNet[key])]) for key in cmdNet))

def PrintResultSummaryVersion2(taskInfo):
    for stackid in taskInfo:
        args, res, retryCount, eff, height, taskCount, commandCount, utilVal, utilitiesList = taskInfo[stackid]
        if res == 'Success':
            succ = 1
            fail = 0
        else:
            succ = 0
            fail = 1
        print("v2", succ, succ+fail, retryCount, globalTimer.GetSimulationCounter(), 
            globalTimer.GetRealCommandExecutionCounter(), eff, height, taskCount, commandCount, utilVal)
        utilString = ""
        for u in utilitiesList:
            utilString += str(u)  
            utilString += " "

        print(utilString)

        #print(' '.join('-'.join([key, str(cmdNet[key])]) for key in cmdNet))


def StartEnv():
    while(True):
        envArgs.sem.acquire()
        if envArgs.exit == True:
            ipcArgs.sem[0].release() # main controller
            return

        StartEnv.counter += 1
        if GLOBALS.GetDomain() != "SDN":
            if StartEnv.counter in problem_module.eventsEnv:
                eventArgs = problem_module.eventsEnv[StartEnv.counter]
                event = eventArgs[0]
                eventParams = eventArgs[1]
                t = threading.Thread(target=event, args=eventParams)
                t.setDaemon(True)  # Setting the environment thread to daemon because we don't want the environment running once the tasks are done
                t.start()
        ipcArgs.sem[0].release()

def add_tasks(tasks):
    current_counter = GetNewTasks.counter
    if current_counter + 1 not in problem_module.tasks:
        problem_module.tasks[current_counter + 1] = tasks
    else:
        problem_module.tasks[current_counter + 1] += tasks

def raeMult():
    ipcArgs.sem = [threading.Semaphore(1)]  #the semaphores to control progress of each stack and master
    ipcArgs.nextStack = 0                 #the master thread is the next in line to be executed, which adds a new stack for every new task
    ipcArgs.threadList = [] #keeps track of all the stacks in RAE Agenda
    lastActiveStack = 0 #keeps track of the last stack that was Progressed
    numstacks = 0 #keeps track of the total number of stacks
    GetNewTasks.counter = 0
    StartEnv.counter = 0
    taskInfo = {}

    envArgs.sem = threading.Semaphore(0)
    envArgs.exit = False

    envThread = threading.Thread(target=StartEnv)
    #startTime = time()
    envThread.start()


    while (True):
        #if ipcArgs.nextStack == 0 or ipcArgs.threadList[ipcArgs.nextStack-1].isAlive() == False:
        if True:
            ipcArgs.sem[0].acquire()
            if numstacks == 0 or BeginFreshIteration(lastActiveStack, numstacks, ipcArgs.threadList) == True: # Check for incoming tasks after progressing all stacks

                taskParams = GetNewTasks()
                if taskParams != []:

                    for newTask in taskParams:
                        numstacks = numstacks + 1
                        raeArgs = GLOBALS.RaeArgs()
                        raeArgs.stack = numstacks
                        raeArgs.task = newTask[0]
                        raeArgs.taskArgs = newTask[1:]

                        ipcArgs.sem.append(threading.Semaphore(0))
                        ipcArgs.threadList.append(threading.Thread(target=CreateNewStack, args = (taskInfo, raeArgs)))
                        ipcArgs.threadList[numstacks-1].start()

                lastActiveStack = 0 # for the environment
                envArgs.sem.release()
                ipcArgs.sem[0].acquire()

                if GLOBALS.GetDomain() == "SDN":
                    UpdateCommandStatus()
                globalTimer.IncrementTime()

            if numstacks > 0:
                res = GetNextAlive(lastActiveStack, numstacks, ipcArgs.threadList)

                if res != -1:
                    ipcArgs.nextStack = res
                    lastActiveStack = res
                    ipcArgs.sem[res].release()
                else:
                    if noNewTasks():
                        envArgs.exit = True
                        envArgs.sem.release()
                        break
            else:
                ipcArgs.sem[0].release()

    if GLOBALS.GetShowOutputs() == 'on':
        print("----Done with RAE----\n")
        PrintResult(taskInfo)
    else:
        PrintResultSummaryVersion2(taskInfo)
        #globalTimer.Callibrate(startTime)

    return taskInfo # for unit tests

def HandleTermination(signalId, frame):
    methodUtil, planningTime = GetBestTillNow()
    method, util = methodUtil
    HandleTermination.q.put((method, util, planningTime))
    sys.exit()
HandleTermination.q = None 

def CallPlanner(pArgs, queue):
    """ Calls the planner according to what the user decided."""
    if GLOBALS.GetPlanner() == "UPOM":

        HandleTermination.q = queue
        signal.signal(signal.SIGTERM, HandleTermination)
        
        if GLOBALS.GetDoIterativeDeepening() == True:
            d = 5
            while(d <= GLOBALS.GetMaxDepth()):
                pArgs.SetDepth(d)
                methodUtil, planningTime = UPOM_Choice(pArgs.GetTask(), pArgs)
                method, util = methodUtil
                d += 5
        else:
            d = GLOBALS.GetMaxDepth()
            pArgs.SetDepth(d)
            methodUtil, planningTime = UPOM_Choice(pArgs.GetTask(), pArgs)
            method, util = methodUtil

    elif GLOBALS.GetPlanner() == "RAEPlan":

        pArgs.SetDepth(GLOBALS.GetMaxDepth())
        methodUtil, planningTime = RAEplan_Choice(pArgs.GetTask(), pArgs)
        method, util = methodUtil

    else:
        print("Invalid planner")
        exit()


    queue.put((method, util, planningTime))

def PlannerMain(task, taskArgs, queue, candidateMethods, state, aTree, curUtil):

    SetMode('Counter') #Counter mode in simulation
    GLOBALS.SetPlanningMode(True)
    #RemoveLocksFromState()

    pArgs = PlanArgs()

    pArgs.SetStackId(1) # Simulating one stack now
    # TODO: Simulate multiple stacks in future
    
    pArgs.SetTask(task)
    pArgs.SetTaskArgs(taskArgs)
    pArgs.SetCandidates(candidateMethods)

    pArgs.SetState(state)
    pArgs.SetActingTree(aTree)
    pArgs.SetCurUtil(curUtil)

    CallPlanner(pArgs, queue)

    