def first_occ(a,size,i,val):
    j = size
    if i==size:
        return

    first_occ(a,size,i+1,val)

    if(a[i]==val and j>i):
        j=i
        print(i)
        return
    else:
        return
        

        
        

arr = [6,3,5,3,9]
print(first_occ(arr,5,0,3))
