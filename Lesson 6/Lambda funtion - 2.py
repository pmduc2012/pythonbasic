__author__ = 'Admin'
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# Funtion 1: use lambda
oddnum = filter(lambda x: x % 2 != 0, foo)
print(sum(list(oddnum)))

# Funtion 2: use lambda
import functools

foo2 = []
for num in foo:
    if num % 2 != 0:
        foo2.append(num)
sum = functools.reduce(lambda x,y : x + y, foo2)
print(sum)

# Funtion 3: use def funtion
def add(x,y):
    return x + y
foo3 = []
for num in foo:
    if num % 2 != 0:
        foo3.append(num)
sum = functools.reduce(add,foo3)
print(sum)