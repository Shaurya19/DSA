# Naive Aprroach

def printUnion(a,b):
    c = a+b
    c.sort()

    for i in range(len(c)):
        if (i == 0 or c[i] != c[i-1]):
            print(c[i],end = " ")

a = [2,4]
b = [3,4]

printUnion(a,b)