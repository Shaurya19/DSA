l = [10,20,30,40,50]
print(l)
print(l[3])
print(l[-2])

l.append(30)
print(l)
l.insert(1,15)
print(l)
print(l.count(30))
print(l.index(30)) # Gives the first occurence
print(l.index(30,4,7)) 