# One transversal


def secmax(l):
    if len(l)<=1:
        return None

    lar = l[0]
    slar = None

    for i in l[1:]:
        if i > lar:
            slar = lar
            lar = i
        # Imp and tricky    
        elif i != lar:
            if slar == None or slar<i:
                slar = i
    
    return slar


lst = []

n= int(input('Enter the number of elements'))

for i in range(0,n):
    element = int(input())
    lst.append(element)

print(secmax(lst))