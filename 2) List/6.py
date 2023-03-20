# Average of a list

def odd_even(l):
    o =[]
    e=[]
    for x in l:
        if x%2==0:
            e.append(x)
        else:
            o.append(x)
    
    return e,o # This returns a tuple


l = [5,7,10,13,20,27,30,40]
even,odd = odd_even(l) # Unpacking the tuple as a 2 lists

print(even)
print(odd)