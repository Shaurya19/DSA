def rev(l):
    if len(l)<=1:
        return l
    revl = []
    
    i=len(l)- 1
    while(i>=0):
        revl.append(l[i])
        i=i-1

    return revl

n = int(input())
lst = []

for i in range(n):
    ele = int(input())
    lst.append(ele)

print(rev(lst))
