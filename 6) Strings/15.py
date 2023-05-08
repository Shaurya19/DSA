def leftmost(str):
    count = [0]*256

    for i in range(len(str)):
        count[ord(str[i])] += 1
    for i in range(len(str)):
        if count[ord(str[i])]>1:
            return i

    return -1