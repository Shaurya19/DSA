# Naive Solution

def lastOcc(l,x):
    for i in reversed(range(len(l))):
        if l[i] == x:
            return i
    return -1

a = [1,2,3,4,5,6]
n = int(input())

print(lastOcc(a,n))

# TC: O(n)