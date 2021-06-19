import time
import timeit

import numpy as np


def squareAndSort(numList):

    leftIndex = 0
    rightIndex = len(numList) - 1
    result = np.zeros(len(numList))
    #for index, element in reversed(list(enumerate(numList))):
    for index in range(len(numList)-1,0,-1):
        
        if(numList[leftIndex] < 0 and abs(numList[leftIndex]) > numList[rightIndex]):
            result[index] = np.square(numList[leftIndex])
            leftIndex += 1
        else:
            result[index] = np.square(numList[rightIndex])
            rightIndex -= 1

    print(result)    
    return result

begin = time.time()

inputList = np.sort(np.random.randint(-20, 20, 5))
print(inputList)
end = time.time()

# total time taken
print(f"Total runtime of the program is {end - begin}")

t = timeit.Timer(lambda: squareAndSort(inputList))
print(t.timeit(number=1))
