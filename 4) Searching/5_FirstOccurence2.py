def firstOccurence(arr,s,e,x):
    if s > e:
        return -1
    mid = (s + e)//2

    if x > arr[mid]:
        return firstOccurence(arr,mid+1,e,x)
    elif x < arr[mid]:
        return firstOccurence(arr,s,mid-1,x)
    else:
        if mid == 0 or arr[mid - 1] != arr[mid]:
            return mid
        else:
            return firstOccurence(arr,s,mid-1,x)
        
a = [10,20,30,30,30,40,50,60]
l = len(a)

item = int(input("Enter the element you'd want to search: "))
result =  firstOccurence(a, 0, l-1, item)

if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found at {} index".format(item, result))

# TC: O(log n)
# AS: O(log n)