from collections import defaultdict
n,m = input().split()
n=int(n)
m=int(m)
a=[]
b=[]
for i in range(n):
    a.append(str(input()))
for i in range(m):
    b.append(str(input()))
    
for i in range(m):
    count=0
    for j in range(n):
        if a[j]==b[i]:
            count+=1
            print(j+1,end=' ')
    if count==0:
        print(-1)
    else:
        print() 