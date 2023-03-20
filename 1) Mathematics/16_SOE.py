# Efficient SOE

def sieve(n):
    if n<= 1:
        return
    
    isPrime = (n+1)*[True]

    i = 2

    while i*i <= n:
        if isPrime[i]:
            for j in range(2*i,n + 1, i):
                isPrime[j] = False
        i += 1

    for i in range(2,n+1):
        if isPrime[i]:
            print(i, end = " ")

sieve(18) 