def fact(n):
    ans = 1

    for i in range(2,n+1):
        ans = ans*i

    return ans

print(fact(5))