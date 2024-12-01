INPUT_FILE_PATH = "input.txt"

import os, sys

list1: list[int] = []
list2: list[int] = []
elem: int = 0

f = open(os.path.join(sys.path[0], INPUT_FILE_PATH),'r')
inputfile = [a.replace("\n", "") for a in f.readlines()]

for line in inputfile:
    temp: list[str] = line.split("   ")
    list1.append( int(temp[0]) )
    list2.append( int(temp[1]) )

list1.sort()
list2.sort()

for i, elem1 in enumerate(list1):
    elem = elem + abs(list2[i] - elem1)

print(elem)

###### PART TWO ######
similarity: int = 0

for elem1 in list1:
    for elem2 in list2:
        if elem1 == elem2:
            similarity = similarity + elem1

print(similarity)
