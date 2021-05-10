import numpy
n,m=map(int,input().split())
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
b=numpy.array(b)
c=numpy.min(b,axis=1)
print(numpy.max(c))