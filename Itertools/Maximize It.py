from itertools import product
t, m =map(int,input().split())
ls = []


for i in range(t):
    tmp = map(int,input()[1:].split())
    tmp2 = [x**2 for x in tmp]
    ls.append(tmp2)
max=0
for i in product(*ls):
    pro=0
    for j in i:
        pro+=j
    if (pro%m)>max:
        max=pro%m
print(max) 