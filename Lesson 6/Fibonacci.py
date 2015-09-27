__author__ = 'Admin'
def Fibonaccinum(n: int):
    if n <= 2:
        return 1
    else:
        return Fibonaccinum(n-2) + Fibonaccinum(n-1)

print(Fibonaccinum(3))