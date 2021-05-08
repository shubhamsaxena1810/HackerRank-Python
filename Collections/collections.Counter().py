from collections import Counter
n=int(input())
a=list(map(int,input().split()))
a=Counter(a)
c=int(input())
earn=0
for i in range(c):
    n,m=input().split()
    n=int(n)
    m=int(m)
    if n in a and a[n]>0:
        a[n]=a[n]-1
        earn+=m
print(earn)