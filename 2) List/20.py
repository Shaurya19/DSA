# Method 2

def isSorted(l):
    sl = sorted(l)

    if l == sl:
        return True
    else:
        return False

lst = [10,20,30,60,50]

if isSorted(lst):
    print("Yes")
else:
    print("No")