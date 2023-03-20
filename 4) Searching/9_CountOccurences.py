# Naive Solution - Linear Transversal O(n)
# Better Solution - Simple Binary Search O(log n + n) - this is because after finding the
# the element we need to check how many times it is reapreated and thus that can 
# happen n times

# Efficiet Soln: using first occurence and last occurence TC: O(log n)

def firstOccurence(arr,s,e,x):
    
    while s<=e:
        mid = (s + e)//2

        if x > arr[mid]:
            s = mid + 1
        elif x < arr[mid]:
            e = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                e = mid - 1

def LastOccurence(arr,s,e,x):
    
    while s<=e:
        mid = (s + e)//2

        if x > arr[mid]:
            s = mid + 1
        elif x < arr[mid]:
            e = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] != arr[mid]:
                return mid
            else:
                s = mid + 1

def CountOccurences(l,x):
    first = firstOccurence(l,0,len(l)-1,x)
    if first == -1:
        return -1
    else:
        return LastOccurence(l,0,len(l)-1,x) - first + 1
        
a = [10,20,30,30,30,40,50,60]
l = len(a)

item = int(input("Enter the element you'd want to search: "))
result =  CountOccurences(a,item)

if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found {} times".format(item, result))