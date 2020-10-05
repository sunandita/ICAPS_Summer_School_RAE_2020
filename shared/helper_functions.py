def ChooseRandom(l):
    random.shuffle(l)
    return l[0]

def addEfficiency(e1, e2):
    if e1 == float("inf"):
        return e2
    elif e2 == float("inf"):
        return e1
    elif e1 == 0 and e2 == 0:
        return 0
    else:
        return e1 * e2 / (e1 + e2)

def PrintList(list):
    if list == None:
        print('[ None ]')
    else:
        print('Refinement list: [', ' '.join(item.method.__name__ for item in list), ']')

def TakeAvg(eList):
	#total = float("inf")
    total = 0
    for eff in eList:
        total += eff
	#return total * len(eList)
    return total / len(eList)
