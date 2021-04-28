import random
# Selection sort from https://stackoverflow.com/questions/48603533/python-selection-sort-with-nested-while-loop/57749692

# Generates an unsorted list of length X
listLength = int(input("\nrandom number list length: "))

unsortedList = []
for x in range (listLength):
    getRandNum = random.randint(0,9)
    unsortedList.append(getRandNum)



# Selection sort into sorted list
def selectionsort(l): # l is passed from our print statement on line 27
    i = 0
    while i < len(l) - 1 :
        for j in range(i+1 , len(l)):
            if l[i] > l[j]:
                (l[i], l[j]) = (l[j], l[i]) #swaps values i and j
        i += 1
    return(l)

comparisons = ((listLength*(listLength-1))/2)

print(str("\nunsorted list\n")+str(unsortedList))
print(str("\nsorted list\n")+str(selectionsort(unsortedList)))
print(str("\nnumber of comparisons for selection sort is always 'n*(n-1)/2' \ncomparisons made: ")+str(int(comparisons)))