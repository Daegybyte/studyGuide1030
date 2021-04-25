import math
lengthOfList = int(input("length of list? "))
guesses = math.ceil(math.log2(lengthOfList))
print(str("Best number of guesses: ")+str(guesses))
