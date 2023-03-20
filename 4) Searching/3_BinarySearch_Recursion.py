
def Binsearch(arr,s,e,item):

    if(s <= e):
        mid = s + (s + e)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            Binsearch(arr,mid+1,e,item)
        else:
            Binsearch(arr,s,mid-1,item)
    else:
        return -1
    
a = [10,20,30,40,50,60]
l = len(a)

item = int(input("Enter the element you'd want to search: "))
result =  Binsearch(a, 0, l-1, item)

if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found at {} index".format(item, result))

# TC: O(log n)
# AS: O(log n)
# Thats why iterative method is better because it needs less AS.