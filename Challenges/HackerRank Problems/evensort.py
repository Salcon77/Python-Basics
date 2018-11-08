def segregateEvenOdd(a):
    counter = 0
    x = 0
    # we need to find the len of a -1 so we can index the last element of the list
    y = len(a) - 1
# x is at 0 and y is the length of the list -1 this loop will continue until x is greater than y
    while x < y:

        # we check for odds on the right
        while(a[x] % 2 == 0):
             x = x+1

        # we check for evens on the left
        while (a[y] % 2 == 1 ):
            y = y-1


        # we swap
        if (x<y):
            # the swap has to occur in the same line
            a[x], a[y] = a[y], a[x]
            x = x + 1
            counter=counter+1


    return a, counter

arr = [13,10,21,20,20,20,20]

print(segregateEvenOdd(arr))