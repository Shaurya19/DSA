# Sorting according to x and y values both

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __lt__(self,other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

l = [Point(7,15),Point(10,5),Point(7,8)]
l.sort()

for i in l:
    print(i.x,i.y)