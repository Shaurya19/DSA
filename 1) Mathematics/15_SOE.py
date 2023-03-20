# Printing prime numbers

def prime(n):

    for i in range(2,n):
        if n%i == 0:
            return False
        
    return True

def SOE(n):

    for i in range(1,n+1):
        if prime(i):
            print(i)

SOE(23)