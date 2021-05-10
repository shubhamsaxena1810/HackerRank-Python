import numpy
n,m,p=map(int,input().split())
N=[]
M=[]
for i in range(n):
    a=list(map(int,input().split()))
    N.append(a)
for i in range(m):
    a=list(map(int,input().split()))
    M.append(a)
N=numpy.array(N)
M=numpy.array(M)
print(numpy.concatenate((N,M),axis=0))            
