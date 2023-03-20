# Efficient Solution with divisors in sorted order

def div(n):
    i=1

    while i*i <n :
        if n%i == 0:
            print(i)

        i += 1

    while (i >= 1):
        if n%i == 0:
            if n%i == 0:
                print(n//i)
            i -= 1

div(64)