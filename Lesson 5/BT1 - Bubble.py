import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
CharList = []
for i in range(20):
    j = random.randint(5,10)
    CharList.append(''.join(random.choice(alphabet) for _ in range(j)))

print(CharList)

CharList2 = []
for char in CharList:
    char2 = ''.join(sorted(char))
    char3 = ''.join(reversed(char2))
    CharList2.append(char3)

print(CharList2)

CharList3 = sorted(CharList2)
CharList4 = reversed(CharList3)
print(list(CharList4))



