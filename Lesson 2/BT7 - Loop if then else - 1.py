'''number = 0
while number < 5 or number > 10:
    number = int(input('Input a number between 5 and 10: '))
    for i in range (1, number + 1):
        for j in range (1, i + 1):
            print(j, end="")
        print("")
'''
while True:
    number = 1
    while number%2==1:
        number = int(input('Please enter a ood number: '))
        if number % 2 == 0:
            print('Sorry, please enter ood number')
            break
        for i in range(number,0,-2):
            print((str(i)*i).center(number*len(str(number))))