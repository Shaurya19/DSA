# Sum of digits

def sod(n):
    if n<10:
        return n
    
    return sod(n//10)+n%10

print(sod(134))