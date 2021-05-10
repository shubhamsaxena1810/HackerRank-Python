import numpy
n=int(input())
b1=[]
b2=[]
for i in range(n):
    a=list(map(int,input().split()))
    b1.append(a)
for i in range(n):
    a=list(map(int,input().split()))
    b2.append(a)
res=numpy.dot(b1,b2)
print(res)
