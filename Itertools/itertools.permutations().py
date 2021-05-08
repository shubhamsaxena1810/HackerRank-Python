import itertools
s,n=input().split()
s=list(str(s))
n=int(n)
s=sorted(s)
for i in list(itertools.permutations(s,n)):
    print(''.join(i))