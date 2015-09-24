import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
CharList = []
for i in range(10):
    j = random.randint(5,10)
    CharList.append(''.join(random.choice(alphabet) for _ in range(j)))
#print(CharList)
#Create random string list.

CharList2 = []
for char in CharList:
    char2 = ''.join(sorted(char))
    char3 = ''.join(reversed(char2))
    CharList2.append(char3)
#print(CharList2)
# Sort z -> a each items of CharList2

CharList3 = sorted(CharList2)
CharList4 = reversed(CharList3)
# Sort z -> a of
print(list(CharList4))