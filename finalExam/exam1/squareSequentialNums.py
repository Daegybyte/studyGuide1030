#This program sums the squares of sequential numbers a user determined number of times

numToSquare = int(input("num to start: "))
numTimes = int(input("repeat times: "))
sumOfSquares = 0

for x in range(numTimes):
    sumOfSquares += (numToSquare*numToSquare)
    numToSquare += 1
print(str(sumOfSquares))
