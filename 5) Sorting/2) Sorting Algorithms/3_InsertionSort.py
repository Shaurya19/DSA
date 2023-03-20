"""
Worst Case: O(n^2)
In-Place and stable
Applications: For small arrays (Tim Sort and Intra Sort)
Best Case: O(n)

The array is sorted from the left side and the next element is
inserted in the sorted part by comparing it with each sorted element 

"""

def insertSort(l):
    n = len(l)

    for i in range(1,n):
        x = l[i]
        j = i-1

        # Shifting elements to the right which are greater than 
        # the first element in the unsorted part
        while j>=0 and x < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = x # Imp to understand why its j+!

    return l

a = [12,10,8,5,14]

print(insertSort(a))