# Efficient Solution
# The divisors are not printed in a sorted order
def div(n):
    i=1
    while(i*i<=n):
        if n%i == 0:
            print(i)
            if(i!=n/i):
                print(n/i)
        i += 1

div(25)