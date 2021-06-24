import numpy as np
import timeit
import BubbleSort
from copy import copy

def partition(list):
    
    pivot = len(list) -1
    i = -1
    for j in range (pivot):
        if (list[j] <= list[pivot]):
            i+=1
            list[i],list[j]=list[j],list[i]
        
    i+=1

    index = i
    for number in np.roll(list[i:],1):
        list[index]= number
        index+=1
    
    pivot = i 
    
    return pivot

def quickSort(inputList):
    pivot = partition(inputList)
    #print(pivot)
    if(pivot> 0):
        leftPart = inputList[0:pivot]
        quickSort(leftPart)
    if(pivot<len(inputList)-1):
        rightPart = inputList[pivot+1:]
        quickSort(rightPart)

    #print(inputList)


inputList = np.random.randint(-100, 100, 10000)
inputList1 = copy(inputList)
#print(inputList)
t = timeit.Timer(lambda:quickSort(inputList))
print('Qucik sort time ', t.timeit(number=1))

t = timeit.Timer(lambda:BubbleSort.bubbleSort(inputList1))
print('Bubble sort time ', t.timeit(number=1))
