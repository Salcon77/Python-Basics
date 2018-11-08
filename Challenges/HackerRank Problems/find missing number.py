"""You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to
 find the missing integer."""

def missNumber(Alist):
    x = sum(Alist)
    n = len(Alist)
    total = (n+1)*(n+2)/2
    z = total - x


    print(z)

test = [1,2,3,5]
print(len(test))
missNumber(test)