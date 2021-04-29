n1 = int(input("first num: "))
n2 = int(input("second num: "))
n3 = int(input("third num: "))

theMax = 0

if (n1 > n2 and n1 > n3):
    theMax = n1
elif(n2 > n1 and n2 > n3):
    theMax = n2
else:
    theMax = n3

print(theMax)