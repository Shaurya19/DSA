# Set Comprehensions

l = [10,20,30,4,10,20,7,4,3]

s1 = {x for x in l if x%2==0}
s2 = {x for x in l if x%2!=0}

print(s1)
print(s2)
# Sets only have unique values
# Order is not defined