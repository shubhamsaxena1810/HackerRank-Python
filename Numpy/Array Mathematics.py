import numpy
n,m=map(int,input().split())
for i in  range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split())) 
    print(numpy.add(a,b))
    print(numpy.subtract(a,b))
    print(numpy.multiply(a,b))
    print(numpy.divide(a,b))
    print(numpy.mod(a,b))
    print(numpy.power(a,b))