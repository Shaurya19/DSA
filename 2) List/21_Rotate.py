l = [10,20,30,40]
r = 2

while(r>0):
    l = l[1:] + l[0:1]
    r =r -1

print(l)

l.append(l.pop(0))
print(l)

x = l[0]

for i in range(1,len(l)):
    l[i-1] = l[i]

l[len(l)-1] = x
print(l)

print(4//3)