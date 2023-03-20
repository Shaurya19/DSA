'''
TC: 0(n^2)
- Does less memory writes compared to Quick Sort, Merge Sort, Insertion Sort, etc. But cycle sort is 
optimal in terms of memory writes
- Basic idea of Heap Sort
- Not stable
- Inplace - does not require extra memory for sorting 

In selection sort we keep finding the smallest element and putting them in the right position in each pass
'''

def selectSort(l):
    n = len(l)

    for i in range(0,n-1):
        min_ind = i
        for j in range(i+1,n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind],l[i] = l[i],l[min_ind]

    return l

a = [10,14,12,18,13]

print(selectSort(a))
