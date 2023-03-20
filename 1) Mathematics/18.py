def pow(x,n):
    if n==0:
        return 1
    
    temp = pow(x,n//2)
    temp = temp * temp

    if n%2 == 0:
        return temp
    else:
        return temp*x
    
print(pow(3,4))