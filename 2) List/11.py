# Getting a list smaller than x using comprehensions

def getsmaller(l,x):
    return[e for e in l if e<x]

l = [9,15,12,3,7,11]

x=10
print(getsmaller(l,x))