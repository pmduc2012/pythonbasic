n1 = int(input('Press number 1: '))
n2 = int(input('Press number 2: '))
Gcd = 1
k = 2
if n1 ==0 or n2 == 0:
    print('Gcd of',n1,'and',n2,'is:',max(abs(n1),abs(n2)))
else:
    while k <=abs(n1) and k <=abs(n2):
        if n1 % k == 0 and n2 % k == 0:
            Gcd = k
        k+=1
    print('Gcd of', n1, 'and',n2,'is:', Gcd)
