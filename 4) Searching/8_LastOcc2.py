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
        
a = [10,20,30,30,30,40,50,60]
l = len(a)

item = int(input("Enter the element you'd want to search: "))
result =  LastOccurence(a, 0, l-1, item)

if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found at {} index".format(item, result))

# TC: O(log n)
# AS: O(1)