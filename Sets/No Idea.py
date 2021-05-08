n,m=input().split()
n=int(n)
m=int(m)
L=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A=set(A)
B=set(B)
count=0
for i in L:
    if i in A:
        count+=1
    elif i in B:
        count-=1
    else:
        continue
print(count)
