n = int(input("start n: "))
numEvens = 0
numOdds  = 0
numLoops = 0


while(n !=1):
    if(n%2 == 0):
        numEvens+=1
        n = n/2
        numLoops+=1
        
    else:
        numOdds+=1
        n = (3*n)+1
        numLoops+=1


print(str("\nn: ")+str(n))
print(str("times even: ")+str(numEvens))
print(str("times odd: ")+str(numOdds))
print(str("times looped: ")+str(numLoops))