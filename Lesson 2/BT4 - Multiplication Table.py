'''
def table(rows, columns):
    print('\t\tMultiplication Table')
    i = ''
    for column in range(1,columns + 1):
        i = i + str(column) + '\t'
    print('\t' + i)
    print('-'*38)
    for row in range(1,rows + 1):
        i = ''
        for column in range(1,columns + 1):
            i = i + str(row*column) + '\t'
        print(str(row) + '|' + '\t' + i)
table(9,9)
'''
print('\t\t\tMultiplication Table')
print('   ', end='')
for i in range (1,10):
    print('%4d' % i, end='')
print()
print('-'*38)
for j in range(1,10):
    print(j,'|',end='')
    for k in range(1,10):
        print('%4d' % (j * k), end='')
    print()