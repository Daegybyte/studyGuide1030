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
