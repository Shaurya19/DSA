# Partition of an array

def partition(arr,p):
    n = len(arr)
    arr[p],arr[n-1] = arr[n-1],arr[p]
    temp = []

    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)
    
    for x in arr:
        if x>arr[n-1]:
            temp.append(x)

    return temp

a = [5,13,6,9,12,8,11]

print(partition(a,5))

# TC: 0(n)
# AS: 0(n) 

