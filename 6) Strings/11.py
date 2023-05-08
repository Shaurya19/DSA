# Program to check if a string is a subsequence i.e some characters might be removed but the order 
# of the remaining characters is same as that of the original string

s1 = "geeksforgeeks"
s2 = "grges"

i, j = 0, 0

while (i<len(s1) and j<len(s2)):
    if s1[i] == s2[j]:
        j+=1
    i+=1
if j == len(s2):
    print(True)
else:
    print(False)