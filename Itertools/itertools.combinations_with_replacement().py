import itertools
A,n=input().split()
A=str(A)
n=int(n)
A=sorted(A)
for i in list(itertools.combinations_with_replacement(A,n)):
    print(''.join(i))