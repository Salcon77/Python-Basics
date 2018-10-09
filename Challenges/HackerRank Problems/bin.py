def getIntegerComplement(n):
    x=(bin(n)[2:])
    print ((x))


    x=str(x)
    listx=(list(x))
    t=len(x)
    # this inverts 1s into 0s and 0s into 1s in the list
    for i in range(t):
        if listx[i] == '1':
            listx[i]='0'
        else:
            listx[i]='1'
    result =''

    # this turns the list into one number [1,2,4] into 124
    for element in listx:
        result = result+(element)

    print (result)
    # convert the str into a int with base 2
    result = int(result, 2)
    print(result)


    #y = x[len(x) - 1:0:-1] + x[0]"""



getIntegerComplement(50)