__author__ = 'duc'

import random

numList = []

for i in range(20):
    numList.append(random.randint(1, 100))

print(numList)

for j in range(1, len(numList) + 1):
    for k in range(j - 1, 0, -1):
        if numList[k] < numList[k - 1]:
            temp = numList[k]
            numList[k] = numList[k - 1]
            numList[k - 1] = temp
        else:
            break

print(numList)
