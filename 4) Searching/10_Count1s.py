# Count 1's in a Sorted Binary List
# Naive Soln: Simple Transversal TC: O(log n)
# Efficient: Find first occurence O(log n)

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
        
a = [0,0,0,0,1,1,1,1]
l = len(a)

result =  l - firstOccurence(a, 0, l-1, 1) 

if result == -1:
    print("The item {} was not found".format(1))
else:
    print("The value {} was found {} times".format(1, result))

