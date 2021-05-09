n,m=map(int,input().split())
b=[]
for i in range(m):
    b.append(list(map(float,input().split())))

for i in list(zip(*b)):
    print('%0.1f'%(sum(i)/len(i)))