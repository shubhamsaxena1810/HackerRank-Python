import itertools
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(itertools.product(A,B))
for i in C:
    print(i,end=' ')