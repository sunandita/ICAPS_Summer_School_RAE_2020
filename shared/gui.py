__author__ = 'patras'
#!/usr/bin/python

import GLOBALS

def Simulate(*t):
    if (GLOBALS.GetPlanningMode() == True or GLOBALS.GetShowOutputs() == 'off'):
        return
    else:
        guiFile = open("../hostdir/Output.txt","a") 
        t1 = ' '.join(map(str, t))
        guiFile.write(t1)
        guiFile.close()

def start(domain, rv):
    if (GLOBALS.GetShowOutputs() == 'on'):
        guiFile = open("../hostdir/Output.txt","w") 
        guiFile.close()