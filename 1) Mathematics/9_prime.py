def check_prime(n):
    c = 0

    for i in range(2,n):
        if n%i == 0:
            c+=1

    return c==0

print(check_prime(7))