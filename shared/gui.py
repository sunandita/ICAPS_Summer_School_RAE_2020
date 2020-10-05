__author__ = 'patras'
#!/usr/bin/python

from tkinter import *
from queue import Queue
import GLOBALS
import turtle

globalQueue = Queue()

class GUI():
    def __init__(self, domain, rv):
        self.domain = domain
        if domain == 'IP_':
            turtle.Screen()
            #tdraw.draw_problem(title="IP_1", rv=rv)
            while(True):
                self.simulate()
        else:
            self.root = Tk()
            self.text = Text(self.root)
            self.text.pack()
            self.root.after(1, self.simulate)
            self.root.mainloop()

    def simulate(self):
        if self.domain == 'IP_':
            if globalQueue.empty() == False:
                t = globalQueue.get()
                tdraw.simulate(t)
        else:
            if globalQueue.empty() == False:
                t = globalQueue.get()
                t1 = ' '.join(map(str, t))
                self.text.insert(END, t1)
            self.root.after(1, self.simulate)

def Simulate(*t):
    if (GLOBALS.GetPlanningMode() == True or GLOBALS.GetShowOutputs() == 'off'):
        return
    elif GLOBALS.GetDomain() == "SDN" and GLOBALS.GetShowOutputs() == "on":
        print(t)
    globalQueue.put(t)

def start(domain, rv):
    if (GLOBALS.GetShowOutputs() == 'on'):
        global g
        g = GUI(domain, rv)