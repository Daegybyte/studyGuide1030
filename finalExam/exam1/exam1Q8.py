# limit = 4
# sum = 0
# i = 2
# while(i<=limit):
#     j = 0
#     while(j<i):
#         sum += 1
#         j += 1
#     i+=1
# print(sum)



# counting the number of times a particular line is counted in loops
limit = 4
sum = 0
i = 2
line5 = 0
line10 = 0
line7 = 0
while(i<=limit):
    j = 0
    line5 += 1
    while(j<i):
        line7+=1
        sum += 1
        j += 1
    i+=1
line10 += 1
print(line5)
print(line10)
print(line7)