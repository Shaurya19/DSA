def power(x,n):
    res = 1
    for i in range(n):
        res = res*x
    return res

print(power(3,4))