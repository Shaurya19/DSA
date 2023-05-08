# Check if string is rotated
# Naive Solution

s1 = "ABCD"
s2 = "CDAB"

s = s1 + s1

if s2 in s:
    print("The string is rotated")
else:
    print("Not Rotated")

s1 = "ABCD"
s2 = "CDAB"
flag = False
for i in range(len(s1)):
    temp = ""
    for j in range(len(s1)-1):
        temp = temp + s1[j+1]
    temp = temp + s1[0] 
    if temp == s2:
        flag = True
        break
    s1 = temp

if flag:
    print("The string is rotated")
else:
    print("The string is not rotated")
