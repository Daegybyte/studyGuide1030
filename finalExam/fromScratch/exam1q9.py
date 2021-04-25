# I don't know why thid was on exam 1 other than to test our ability to read pseudocode
import random

repeat = int(input("repeat times: "))

sumOfSquares = 0
for i in range(repeat):
    numToSquare = random.randint(5,19)
    sumOfSquares += numToSquare*numToSquare
sumOfSquares = sumOfSquares/repeat

print(sumOfSquares)

#1000000