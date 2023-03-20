# Sorting user defined objects

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def myFun(p):
    return p.x

l = [Point(7,15),Point(10,5),Point(1,8)]
l.sort(key=myFun)

for i in l:
    print(i.x,i.y)