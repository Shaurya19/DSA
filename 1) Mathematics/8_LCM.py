# Naive

def LCM(a,b):

    res = max(a,b)

    while True:
        if res%a == 0 and res%b == 0:
            return res

        res+=1


print(LCM(6,8))

# Efficient Solution LCM = (a * b) / GCD(Using euclidean algorithm)

        