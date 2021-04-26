n = 1
numEvens = 0
numOdds  = 0


while(n !=1):
    if(n%2 == 0):
        numEvens+=1
        n = n/2
    else:
        numOdds+=1
        n = (3*n)+1


print(numEvens,numOdds)