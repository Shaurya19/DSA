l = [10,20,30,40,50,60,70,80]
l.remove(20)
print(l.pop()) # Removes the last element
print(l.pop(3)) # Removes the element at index 3 from the list
print(l)
del l[1]
print(l)
del l[0:2]
print(l)