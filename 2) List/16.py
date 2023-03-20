# Largest element in a list

def getmax(l):
    if not l: # To check if list is empty
        return 0
    else:
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

print(getmax(lst))