# Dictionary Comprehensions

l1 = [1,3,4,2,5]
d1 = {x:x**3 for x in l1}
print(d1)

d2 = {x:f"ID[x]" for x in range(5)}
print(d2)

l2  = [101,102,103]
l3 = ["gfg","ide","courses"]
d3 = {l2[i]:l3[i] for i in range(len(l2))}
print(d3)

#Better Way

d4 = dict(zip(l2,l3))
print(d4)