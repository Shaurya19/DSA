# Merging two sorted list and returning a sorted list

def merge(a,b):

    res = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0

    while i<m and j<n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    
    if i<m:
        res += a[i:]
    if j<n:
        res += b[j:]

    return res

a = [1,3]
b = [2,4,5,6]

print(merge(a,b))

        
    