# naive approach

def gcf(a,b):
    x = max(a,b)
    y = min(a,b)

    for i in range(y):
        if x%(y-i)==0 and y%(y-i)==0:
            return y-i

print(gcf(12,16))