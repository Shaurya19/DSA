def first_occ(a,size,i,val):
    
    if i==size:
        return

    if(a[size-i-1]==val):
        print(size-i-1)
        i=size-1
        

    return first_occ(a,size,i+1,val)

arr = [6,3,5,3,9]
first_occ(arr,5,0,3)
