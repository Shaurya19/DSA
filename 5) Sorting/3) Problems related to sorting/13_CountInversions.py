# A pair (arr[i],arr[j]) forms an inversion 
# When i<j and arr[i] > arr[j]

#Naive Approach TC: O(n^2)

def CountInv(a):
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                count += 1

    return count

a = [2,4,1,3,5]
print(CountInv(a))
