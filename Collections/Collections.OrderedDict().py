d={}
n=int(input())
for i in range(n):
    z=(input().split())
    a=int(z.pop())
    z=' '.join(z)
    if z in d:
        d[z]=d[z]+a
    else:
        d[z]=a
for i in d:
    print(i,d[i])