# Program to check if the string is a subsequence using recursion

def inSubSeq(s1,s2,m,n):
    if n==0:
        return True
    if m==0:
        return False
    if s1[n-1] == s2[m-1]:
        return inSubSeq(s1, s2, m-1, n-1)
    else:
        return inSubSeq(s1, s2, m-1, n)