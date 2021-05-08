d={}
n=int(input())
a=1
count=0
for i in range(n):
    z=str(input())
    if z in d:
        d[z]=d[z]+a
    else:
        d[z]=a

print(len(d))
for i in d:
    print(d[i],end=' ')