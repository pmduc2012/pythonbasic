x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]
a = []
b = []
zipped = zip(a,b)
i = min(len(x),len(y))
for k in range(0, i):
    if (x[k]+y[k]) <= 10:
        a.append(x[k])
        b.append(y[k])
print(list(zipped))