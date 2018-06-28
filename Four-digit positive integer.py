x  = 5724
print(sum(map(int,str(x))))

y = list(str(x))

for i in reversed(y):
    print (i, end = "")

for i in sorted(y):
    print (i, end = "")