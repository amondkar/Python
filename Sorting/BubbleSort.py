import numpy as np
import timeit

def bubbleSort(inputList):
    notSorted = True
    lastIndex = len(inputList) -1

    while(notSorted):
        notSorted = False
        for i in range(lastIndex):
            if(inputList[i]>inputList[i+1]):
                inputList[i], inputList[i+1] = inputList[i+1],inputList[i]
                notSorted = True
    
    return inputList

inputList = np.random.randint(-100, 100, 10000)

#print(inputList)
#t = timeit.Timer(lambda:bubbleSort(inputList))
#print(t.timeit(number=1))
#print(inputList)