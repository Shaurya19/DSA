# Efficient Solution : Using Binary Search

def SquareBin(n):
    s = 1
    e = n
    ans = -1

    while s<=e:
        mid = (s+e)//2
        msq = mid * mid
        if msq == n:
            return mid
        elif msq > n:
            e = mid - 1
        else:
            s = mid + 1
            ans = mid

    return ans 

print(SquareBin(14))