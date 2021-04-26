#From exam 1, Q10 n = 353
n = int(input("num to run: "))
i = 1
sum = 0

while(i<=n):
    if(i%2 !=0):
        sum = (sum +(1/i))
    else:
        sum = (sum-(1/i))
    i = i +1
print(sum)