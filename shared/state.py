__author__ = 'patras'

from threading import Lock

# importing itertools to evaluate statements in OF
# may want to change logic to not require import
import itertools
import random
import copy

class State():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self.__dict__[key] = StateDict(value)

    def GetFeatureString(self):
        res = ""
        if self != False:
            for (key, val) in vars(self).items():
                res = res + key + " " + val.__str__() + "\n"
        else:
            res = 'False'
        return res[0:-1]

    def __str__(self):
        res = ""
        if self != False:
            for (key, val) in vars(self).items():
                res = res + '   state.' + key + ' =' + val.__str__() + '\n'
        else:
            res = 'False'
        return res

    def copy(self):
        s = State()
        for (key, val) in vars(self).items():
            s.__setattr__(key, copy.deepcopy(val.GetVal()))
            s.__dict__[key].DeleteLocks() # because locks are not picklable
        return s

    def restore(self, s):
        oldKeys = list(self.__dict__.keys())
        for (key, val) in vars(s).items():
            self.__setattr__(key, copy.deepcopy(val.GetVal()))
            oldKeys.remove(key)
        for k in oldKeys:
            del self.__dict__[k]
        return s

    def ReleaseLocks(self):
        for key in self.__dict__:
            self.__dict__[key].ReleaseAllLocks()

    def Print(self):
        print(self)

    def EqualTo(self, s):
        for (key1, val1) in vars(self).items():
            for sub_k1 in val1:
                if key1 not in vars(s):
                    return False
                else:
                    if sub_k1 not in vars(s)[key1]:
                        return False
                    elif vars(s)[key1][sub_k1] != val1[sub_k1]:
                        return False
        return True

class StateDict():
    def __init__(self, d):
        if hasattr(d, '__iter__'):
            self.lock = {}
            for key in d:
                self.lock[key] = Lock()
        else:
            self.lock = Lock()
        self.dict = d

    def GetVal(self):
        return dict(self.dict)

    def __getitem__(self, item):
        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value
        if key not in self.lock:
            self.lock[key] = Lock()

    def __cmp__(self, other):
        return cmp(self.dict, other)

    def __iter__(self):
        return self.dict.__iter__()

    def __str__(self):
        return self.dict.__str__()

    def pop(self, key):
        return self.dict.pop(key)

    def update(self, other):
        return self.dict.update(other)

    def remove(self, key):
        del self.dict[key]

    def keys(self):
        return self.dict.keys()

    def items(self):
        return self.dict.items()

    def AcquireLock(self, *key):
        if len(key) == 1:
            self.lock[key[0]].acquire()
        else:
            self.lock[key].acquire()

    def ReleaseLock(self, *key):
        if len(key) == 1:
            self.lock[key[0]].release()
        else:
            self.lock[key].release()

    def ReleaseAllLocks(self):
        if hasattr(self.lock, '__iter__'):
            for key in self.lock:
                if self.lock[key].locked():
                    self.lock[key].release()
        else:
            if self.lock.locked():
                self.lock.release()

    def DeleteLocks(self):
        self.lock = None

state = State()  # the global state of RAE, this is shared by all stacks

def ReinitializeState():   
    """
    State is reinitialized before every run, useful in batch runs
    """
    global state
    state = State()

def RemoveLocksFromState():
    """
    We get rid of all the locks in the simulated state used in APE-plan because we simulate only one stack.
    """
    state.ReleaseLocks()

def PrintState():
    print(state)

def RestoreState(s):
    state.restore(s)

def GetState():
    return state

#Rigid variables
class RV():
    def __init__(self):
        pass

rv = RV()

def EvaluateParameters(expr, mArgs, tArgs):
    for i in range(0, len(tArgs)):
        globals()[mArgs[i]] = tArgs[i]
    return eval(expr, globals())
    
if __name__=="__main__":
    s = State()
    s.a = {1:3, 2:5}
    s.b = {5:20}
    t = State()
    t.a = {1:0, 2:5}
    t.b = {2:10, 5:20}
    print(s.EqualTo(t))
    t.a[1] = 3
    print(s.EqualTo(t))