# Spliting odd and even numbers from a list by using comprehensions

def getEvenOdd(l):
    even = [x for x in l if x%2==0]
    odd = [x for x in l if x%2!=0]
    return even, odd

l = [10,3,20,5,12]
even, odd = getEvenOdd(l)
print(even)
print(odd)