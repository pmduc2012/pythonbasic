'''while True:
    number = 1
    while number%2==1:
        number = int(input('Please enter a odd number: '))
        if number % 2 == 0:
            print('Sorry, please enter odd number')
            break
        for i in range(number,0,-2):
            print((str(i)*i).center(number*len(str(number))))
'''
a = []
b = []
for i in range(1,101):
    if i%3 == 0:
        a.append(i)
    if i%5 == 0:
        b.append(i)
print('A =',a)
print('B =',b)
