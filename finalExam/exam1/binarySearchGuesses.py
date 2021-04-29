# outputs the optimal number of guesses a binary search will need for any given lenghth of list
import math
lengthOfList = int(input("length of list? "))
guesses = math.ceil(math.log2(lengthOfList))
print(str("Max number of guesses: ")+str(guesses))
