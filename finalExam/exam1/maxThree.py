n1 = int(input("first num: "))
n2 = int(input("second num: "))
n3 = int(input("third num: "))

maxValue = 0

if (n1 > n2 and n1 > n3):
    maxValue = n1
elif(n2 > n1 and n2 > n3):
    maxValue = n2
else:
    maxValue = n3

print(maxValue)