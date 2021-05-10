import numpy
a=numpy.array(list(map(int,input().split())))
b=numpy.array(list(map(int,input().split())))
print(numpy.inner(a,b),numpy.outer(a,b),sep='\n')