# This program creates a fib sequence off of two numbers and repeats until the iteration limit is set and then one extra for good measure

fibonacci = []

previousFib = int(input(str("start one: ")))
thisFib = int(input(str("start two: ")))
iterations = int(input("until: "))

fibonacci.append(previousFib)
print(str(str(len(fibonacci))+str(": ")+str(fibonacci[-1])))
fibonacci.append(thisFib)
print(str(str(len(fibonacci))+str(": ")+str(fibonacci[-1]))) 

while(thisFib<iterations):
    nextFib = thisFib+previousFib
    previousFib = thisFib
    thisFib = nextFib
    fibonacci.append(thisFib)
    print(str(str(len(fibonacci))+str(": ")+str(fibonacci[-1]))) 

   
print("Done")

#print(str(str(len(fibonacci))+str(": ")+str(fibonacci[-1]))) 
#1000000000000
