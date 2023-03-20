def squareFloor(x):
    i = 1
    while i*i <= x:
        i += 1
    return i-1

print(squareFloor(9))

# TC: O(n^1/2)
# AS: O(1)