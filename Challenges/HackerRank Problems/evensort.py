def segregateEvenOdd(a):
    counter = 0
    x = 0
    y = len(a) - 1

    while x < y:
        while(x < y and a[x] % 2 == 0):
             x = x+1


        while (a[y] % 2 == 1 and x < y):
            y = y-1



        if (x < y):
            a[x], a[y] = a[y], a[x]
            x += 1
            counter=counter+1


    return a, counter

arr = [13,10,21,20]

print(segregateEvenOdd(arr))