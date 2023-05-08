# Optimized Solution

s1 = "ABCD"
s2 = "CDAB"

s = s1 + s1

if s2 in s:
    print("The string is rotated")
else:
    print("Not Rotated")