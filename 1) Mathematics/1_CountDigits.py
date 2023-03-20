def count(n):
    ans = 0 

    while n>0:
        n = n//10
        ans = ans + 1

    return ans

print(count(143))

# theta(d)

