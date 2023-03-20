# Naive Approach

def intersection(a,b):
    for i in range(len(a)):
        if i>0 and a[i]==a[i-1]:
            continue # Takes control to for loop
        for j in range(len(b)):
            if a[i] == b[j]:
                print(a[i],end=" ")
                break

a = [1,20,20,40,60]
b = [2,20,40,20]

intersection(a,b)
