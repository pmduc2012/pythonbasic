__author__ = 'Admin'
import math
def Pt(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('Phuong trinh co vo so nghiem')
            else:
                print('Phuong trinh vo nghiem')
        else:
            print(-c/b)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return 'Phuong trinh vo nghiem'
        elif delta == 0:
            return -(b/(2*a))
        else:
            return (-b + math.sqrt(delta))/(2*a), (-b - math.sqrt(delta))/(2*a)

print(Pt(0, 0, 1))