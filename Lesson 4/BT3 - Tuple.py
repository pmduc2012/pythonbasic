numList = [9, 3, 2, 5, 6, 8, 11]

num1 = []
num2 = []

for i in numList:
    if i <= 5:
        num1.append(i)
    else:
        num2.append(i)

num1.sort()
num2.sort()

Result = (num1, num2)
print(Result)