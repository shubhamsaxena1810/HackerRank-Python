import numpy
n,m=map(int,input().split())
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
b=numpy.array(b)
c=numpy.sum(b,axis=0)
prod=1
for i in c:
    prod=prod*i 
print(prod)