# Return the closest element less than a particular value

def findFloor(A,N,X):
        #Your code here
        if X < A[0]:
            return -1
            
        s = 0
        e = N-1
        
        while s <= e:
            mid = (s+e)//2
            if A[mid] > X:
                e = mid-1
                if X > A[e]:
                    return e
                
            elif A[mid] < X:
                s = mid + 1
                
            else:
                return mid - 1
            
a = [1,2,3,4,5]

print(findFloor(a,len(a),4))