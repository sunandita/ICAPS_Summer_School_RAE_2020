__author__ = 'patras'

from time import time
import GLOBALS
import types

class Duration():
    def __init__(self):
        pass

DURATION = Duration()
DURATION.TIME = {}
DURATION.COUNTER = {}

class Timer():
    def __init__(self):
        self.mode = 'Counter'
        self.simCount = 0
        self.realCount = 0

    def SetMode(self, m):
    # Specify whether to use clock or global counter to simulate the running state of commands
        self.mode = m
        if m == 'Counter':
            self.simCount = 0
            self.realCount = 0
        elif self.mode == 'Clock':
            pass
        else:
            print("Invalid mode. Set mode to either 'Counter' or 'Clock'")

    def IncrementTime(self):
        if self.mode == 'Counter':
            mode = GLOBALS.GetPlanningMode()
            if mode == False:
                self.realCount += 1
            else:
                self.simCount += 1

    #def Callibrate(self, startTime):
    #    if self.mode == 'Counter':
    #        secsPerTick = (time() - startTime) / self.now
    #        print("Ticks per second is ", 1 / secsPerTick)

    def IsCommandExecutionOver(self, cmd, start, *cmdArgs):
        mode = GLOBALS.GetPlanningMode()
        if mode == False:
            # in acting mode

            # get the time required depending on mode
            if self.mode == 'Counter':
                cost = DURATION.COUNTER[cmd]
            elif self.code == 'Clock':
                cost = DURATION.TIME[cmd]

            # time may be a function of command parameters
            if type(cost) == types.FunctionType:
                t = cost(*cmdArgs)
            else:
                t = cost
            
            # increment the time depending on the mode
            if self.mode == 'Clock':
                if time() - start < t:
                    over = False
                else:
                    over = True
            elif self.mode == 'Counter':
                self.realCount += t
                over = True

            return over
        else:
            # in planning mode, simulation of each command outcome costs 1 unit of time
            self.simCount += 1
            return True

    def GetSimulationCounter(self):
        return self.simCount

    def GetRealCommandExecutionCounter(self):
        return self.realCount

    def UpdateSimCounter(self, step):
        self.simCount += step

    def ResetSimCounter(self):
        self.simCount = 0

    def GetTime(self):
        mode = GLOBALS.GetPlanningMode()
        if mode == False:
            return self.realCount
        else:
            return self.simCount

globalTimer = Timer()

def SetMode(m):
    globalTimer.SetMode(m)