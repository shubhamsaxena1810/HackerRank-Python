n,m=map(int,input().split())
table=[]
for _ in range(n):
    a=list(map(int,input().split()))
    table.append(a)

s=int(input())
table.sort(key = lambda x: x[s])

for i in table:
    for j in i:
        print(j,end=' ')
    print()