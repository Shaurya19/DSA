def PF(n):
    i = 2
    n1 = n
    while i<= n1/2:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1

PF(39)




