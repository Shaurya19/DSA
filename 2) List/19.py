# Check if list is sorted in ascending order
# Method 1

def checksort(l):
    if len(l)<=1:
        return True

    n = len(l)
    

    for i in range(n-1):
        if l[i]>l[i+1]:
            return False

    return True

n = int(input())

lst = []

for i in range(n):
    element = int(input())
    lst.append(element)

print(checksort(lst))


