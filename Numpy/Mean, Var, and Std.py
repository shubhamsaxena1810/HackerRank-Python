import numpy

n,m=map(int,input().split())

a=numpy.array([list(map(int,input().split())) for i in range(n)])
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
c=numpy.std(a,None)
if c==0:
    print('0.0')
else:
    print('%0.11f'%c)
