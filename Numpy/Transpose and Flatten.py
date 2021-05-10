import numpy
N,M= map(int,input().split())
b=[]
for i in range(N):
    a=(list(map(int,input().split())))
    b.append(a)
b=numpy.array(b)
print(numpy.transpose(b))
print(b.flatten())