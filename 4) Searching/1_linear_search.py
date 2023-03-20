def linear_search(arr, l, item):
    
    for i in range(l):
        if arr[i] == item:
            return i
        
    return -1

arr = [10, 2, 8, 20, 40, 15, 25]
item = int(input("Enter the value you'd want to search: "))

l = len(arr)

result = linear_search(arr,l, item)

if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found at {} index".format(item, result))