n = int(input())

lst=[]
for i in range(n):
    e = int(input())
    lst.append(e)

res=1
temp = []
temp = n*[0]
temp[0] = lst[0]
for i in range(1,n):
    if(lst[res-1]!=lst[i]):
        lst[res] = lst[i]
        res = res+1
        temp.append(lst[i])

print(res)
print(temp)
