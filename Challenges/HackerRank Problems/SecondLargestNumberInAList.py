"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given scores. Store them in a list and find the score of the runner-up.

The first line contains . The second line contains an array   of  integers each separated by a space.
Print the runner-up score.
"""
# Array of random numbers to test
arr =[1,2,6,4,87,-9]

maxNUm = int()
runnerUp = int()
for n in arr:

    if n > maxNUm:
            runnerUp = maxNUm
            maxNUm = n


    elif maxNUm > n > runnerUp:
            runnerUp = n
print(runnerUp)

x=56.0
round (x,2)
print(x)