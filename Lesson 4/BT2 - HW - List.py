fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']

i = []

for fruit in fruits:
    j = fruits.count(fruit)
    i.append(j)
# Create new list with index to join with current list.
result = list(zip(fruits, i))

for k in result:
    while result.count(k) > 1:
        result.remove(k)
# Same exercise in List lesson, remove duplicate items.
print(result)