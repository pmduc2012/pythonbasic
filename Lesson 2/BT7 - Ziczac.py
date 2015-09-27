__author__ = 'Admin'
line = int(input('Nhap so duong ziczac: '))
point = int(input('Nhap so diem tren moi duong: '))

isPrinted = False

for i in range(point):
    for j in range(line*(point - 1) + 1):
        for k in range(1, line + 1):
            if k % 2 != 0:
                if (j + i) == (point - 1) * k or (j - i) == (point - 1) * k:
                    print('*', end='')
                    isPrinted = True
                    break
        if isPrinted == False:
            print(' ',end='')
        isPrinted = False
    print()