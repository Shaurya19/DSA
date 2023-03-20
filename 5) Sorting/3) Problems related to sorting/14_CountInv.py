# Efficient Aprroach using Merge Sort

def CountSort(a,l,m,r):
    left = a[l:m+1]
    right = a[m+1:r+1]

    i,j,count,k = 0,0,0,l

    while i < len(left) and j<len(right):
        if left[i] <= right[j]:  # = sign is imp for stability
            a[k] = left[i]
            i = i+1
            k = k+1
        else:
            a[k] = right[j]
            j = j+1
            k = k+1
            count += len(left) - i

    while i<len(left):
        a[k] = left[i]
        i = i+1
        k = k+1
    while j<len(right):
        a[k] = right[j]
        j = j+1
        k = k+1
    return count



def CountMerge(a,l,r):
    count = 0

    if l<r:
        m = (l+r)//2
        count += CountMerge(a,l,m)
        count += CountMerge(a,m+1,r)
        count += CountSort(a,l,m,r)

    return count

a = [2,4,1,3,5]
print(CountMerge(a,0,len(a)-1))