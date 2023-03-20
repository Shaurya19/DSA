# 3^10 = 3^8 + 3^2
# 10: 1010

def pow(x,n):
    res = 1
    while n>0:
        if n%2 != 0:
            res = res*x
        x = x*x
        n = n//2
    return res

print(pow(2,3))