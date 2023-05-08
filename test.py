def bubblesort(a):

    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]

    print(a)

bubblesort([5,1,3,2])