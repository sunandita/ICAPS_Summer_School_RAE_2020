__author__ = 'patras'
#!/usr/bin/python

import GLOBALS

class GUI():
    def __init__(self, domain, rv):
        self.domain = domain
        self.guiFile = open("../hostdir/Output.txt","w") 

    def simulate(self, t):
        t1 = ' '.join(map(str, t))
        self.guiFile.write(t1)

def Simulate(*t):
    if (GLOBALS.GetPlanningMode() == True or GLOBALS.GetShowOutputs() == 'off'):
        return
    elif GLOBALS.GetDomain() == "SDN" and GLOBALS.GetShowOutputs() == "on":
        print(t)
    else:
        g.simulate(t)

def start(domain, rv):
    if (GLOBALS.GetShowOutputs() == 'on'):
        global g
        g = GUI(domain, rv)