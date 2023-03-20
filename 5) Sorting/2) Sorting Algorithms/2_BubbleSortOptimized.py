# TC: O(n^2)
# Best Case: 0(n)

def bubbleSort(l):
    n = len(l)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1],l[j]
                swapped = True
        if swapped == False: # This means that no sorting 
            # was done and thus list is sorted and no further iterations are needed 
            return l

    return l

a = [10,8,20,5]
print(bubbleSort(a))

