__author__ = 'Admin'
import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
CharList = []
for i in range(10):
    j = random.randint(5,10)
    CharList.append(''.join(random.choice(alphabet) for _ in range(j)))
#Create random string list
print(CharList)
for k in range(0, len(CharList) - 1):
    for l in range(k + 1, len(CharList)):
        if alphabet.index(CharList[k][0]) < alphabet.index(CharList[l][0]):
            temp = CharList[k]
            CharList[k] = CharList[l]
            CharList[l] = temp

print(CharList)