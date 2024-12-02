INPUT_FILE_PATH = "input.txt"

import os, sys

unsafe: list[list[int]] = []

def partone(temp: list[int], store: list[list[int]]):
    inc: bool = False
    dec: bool = False
    for i,val in enumerate(temp):
        if i == len(temp)-1: continue
        elif i == 0:
            if val < temp[i+1] and val + 3 >= temp[i+1]: inc=True 
            elif val > temp[i+1] and val - 3 <= temp[i+1]: dec=True
            else: 
                store.append(temp)
                break
        else:
            if (val + 3 < temp[i+1] and inc) or (val > temp[i+1] and inc):
                store.append(temp)
                break
            elif (val - 3 > temp[i+1] and dec) or (val < temp[i+1] and dec):
                store.append(temp)
                break
            elif val == temp[i+1]:
                store.append(temp)
                break
            else: continue

def partone_ed(temp: list[int]) -> bool:
    inc: bool = False
    dec: bool = False
    for i,val in enumerate(temp):
        if i == len(temp)-1: continue
        elif i == 0:
            if val < temp[i+1] and val + 3 >= temp[i+1]: inc=True 
            elif val > temp[i+1] and val - 3 <= temp[i+1]: dec=True
            else: 
                return False
        else:
            if (val + 3 < temp[i+1] and inc) or (val > temp[i+1] and inc):
                return False
            elif (val - 3 > temp[i+1] and dec) or (val < temp[i+1] and dec):
                return False
            elif val == temp[i+1]:
                return False
            else: continue
    return True

def parttwo(us: list[list[int]]) -> int:
    safe_count: int = 0
    
    for temp in us:
        for slice in range(len(temp)):
            more_temp = [temp[i] for i in range(len(temp)) if i != slice]
            if partone_ed(more_temp):
                safe_count = safe_count + 1
                break
    return safe_count


f = open(os.path.join(sys.path[0], INPUT_FILE_PATH),'r')
inputfile = [a.replace("\n", "") for a in f.readlines()]

for line in inputfile:
    temp: list[int] = [int(i) for i in line.split(' ')]
    partone(temp, unsafe)

safe = parttwo(unsafe)
print(safe)