# Get smaller elements from a list than an inputed number

def smaller(l,x):
    s=[]
    for i in l:
        if i<x:
            s.append(i)

    return s

l = [8,100,20,40,3,7]
x = 10
print(smaller(l,x))

