# Efficient Approach

def intersection(a,b):
    i = 0
    j = 0

    while i<len(a) and j<len(b):
        if i>0 and a[i] == a[i-1]:
            i += 1
            continue
        elif a[i]<b[j]:
            i += 1
        elif a[i]>b[j]:
            j += 1
        else:
            print(a[i],end = " ")
            i += 1
            j += 1

a = [1,20,20,40,60]
b = [2,20,40,20]

intersection(a,b) 