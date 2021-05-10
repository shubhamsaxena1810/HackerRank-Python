import numpy
n=int(input())
b=[list(map(float,input().split())) for i in range(n)]
print(round(numpy.linalg.det(b),2))