# Naive Approach

def firstOcc(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i
        
    return -1

arr=[]

n = int(input("Enter the number of elements: "))

for i in range(n):
    e = int(input())
    arr.append(e)

x = int(input("Enter the number of element: "))

print(firstOcc(arr,n,x))

# TC: O(n)
# AS: O(1)