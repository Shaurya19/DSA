def MyFun(s):
    return len(s)

l = ["gfg","courses","python"]
l.sort(key=MyFun)
print(l)
l.sort(key = MyFun,reverse=True)
print(l)