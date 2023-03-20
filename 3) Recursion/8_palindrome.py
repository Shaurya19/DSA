def pal(str, start, end):
    if start>=end:
        return True

    return(str[start] == str[end] and pal(str,start+1,end-1))

print(pal('shaurys',0,6))
    