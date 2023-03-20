# Array has to be sorted

def Binary_search(arr,l,item):
    s = 0
    e = l
    

    while s<= e:
        m = (s + e) // 2   # or m = s + (e - s)//2 
        # If we calculate the middle index by (s+e)//2 our code is not 100% correct, it contains bugs.
        #That is, it fails for larger values of int variables low and high. Specifically, it fails if the sum of low and high is greater than the maximum positive int value(231 – 1 ).
        if arr[m] == item:
            return m
        elif arr[m] < item:
            s = m + 1
        else:
            e = m-1

    return -1

arr = [10, 2, 8, 20, 40, 15, 25]
item = int(input("Enter the value you'd want to search: "))

l = len(arr)

result =  Binary_search(arr,l-1, item)

if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found at {} index".format(item, result))

# TC: O(log n)
# AS: O(1)