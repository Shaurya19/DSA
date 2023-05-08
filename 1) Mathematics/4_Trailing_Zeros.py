# Trailing Zeros in a factorial
# Keep dividing by 5
# This logic works because for every 5 there is a 2

def count(n):
    
    res = 0

    while n >= 5:
        n //= 5
        res += n

    return res

print(count(10))



    


