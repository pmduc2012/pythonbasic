fruits = ['cam', 'tao', 'nho', 'le', 'tao', 'cam', 'le', 'na']

def deldup(fruits):

    fruits2 = []

    for fruit in fruits:
        if fruits2.count(fruit) == 0:
            fruits2.append(fruit)
    return fruits2

print(deldup(fruits))