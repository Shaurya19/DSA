# Optimized Euclidean Algorithm

def gcd(a,b):

    if b == 0:
        return a

    return gcd(b,a%b)

print(gcd(12,16))