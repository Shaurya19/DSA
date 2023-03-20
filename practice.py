def selection_sort(l):
    n = len(l)

    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i],l[min_index]

    return l

print(selection_sort([10,8,13,4,19]))