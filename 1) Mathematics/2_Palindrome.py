def palindrome(n):
    rev = 0
    n1 = n

    while n>0:
        l = n%10
        rev = rev*10 + l
        n = n//10

    return rev == n1

print(palindrome(101))