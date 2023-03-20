# Difference between lists, tuples and strings

l1 = [10,0,30]
l2 = l1[:]

t1 = (10,20,30)
t2 = t1[:]

s1 = "geeks"
s2 = s1[:]

print(l1 is l2)
print(t1 is t2)
print(s1 is s2)

# Strings and tuples return true because they are immutable