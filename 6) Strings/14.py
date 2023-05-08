# Leftmost repeating characters
# Naive Approach
def leftmost(s):

    s = "cabbad"
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return i

    return -1

print(leftmost("cabbad"))