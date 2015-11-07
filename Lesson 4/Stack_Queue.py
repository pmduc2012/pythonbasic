__author__ = 'MinhDuc'
A = '20+3*4-(5+6)/7'

Infix = []
Postfix = []
Stack = []
Prefix = []

def prec(i):
    if i is '(':
        return 0
    elif i is '+' or i is '-':
        return 1
    elif i is '*' or i is '/':
        return 2

def oper(i):
    if i is '+' or i is '-' or i is '*' or i is '/':
        return 'operator'
    elif i is '(':
        return 'left'
    elif i is ')':
        return 'right'
    else:
        return 'operand'

for j in A:
    Infix.append(j)
print(Infix)

for k in Infix:

    if oper(k) is 'operand':
        Postfix.append(k)
    elif k is '(':
        Stack.append(k)
    elif k is ')':
        stack = Stack.pop()
        while stack is not '(':
            Postfix.append(stack)
            stack = Stack.pop()
    elif oper(k) is 'operator':
        while len(Stack) > 0 and prec(Stack[-1]) >= prec(k):
            Postfix.append(Stack.pop())
        Stack.append(k)

while len(Stack) > 0:
    Postfix.append(Stack.pop())
print(''.join(Postfix))
prec(''.join(Prefix))
