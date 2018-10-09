def findSum(arr, sum):
    x=0
    y=len(arr)-1

    while x <= y:
        if arr[x]+arr[y] == sum and x!=y:
            print(" two numbers in the given list that equal {} are {} and {}".format(sum,arr[x],arr[y]))
            return True
        elif arr[x]+arr[y] < sum:
            x=x+1
        else:
            y=y-1
    return False


array=[1,2,3,4,5,5]
target=10
print(findSum(array,target))
