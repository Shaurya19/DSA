# Second largest element
# Two transversals

def getsecmax(l):
    if len(l)<=1:
        return None

    lar = getmax(l)
    slar = None

    for x in l:
        if(x!=lar):
            if slar==None:
                slar=x
            else:
                slar = max(slar,x)
    return slar

def getmax(l):
    
    res=l[0]
    for i in l:
        if i>res:
            res=i
    return res


lst=[]
n = int(input('Enter the number of elements'))

for i in range(0,n):
    element = int(input())

    lst.append(element)

print(getsecmax(lst))