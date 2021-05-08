import itertools
n=int(input())
s=list(input().split(' '))
x=int(input())
a=[]
b=[]
c=[]
for i in range(1,n+1):
    a.append(i)
for i in list(itertools.combinations(a,x)):
    b.append(i)
for i in range(len(s)):
    if s[i]=='a':
        c.append(i+1)
count=0
for i in range(len(b)):
    for j in range(x):
        if (b[i][j] in c):
            count+=1
            break
print(count/len(b))