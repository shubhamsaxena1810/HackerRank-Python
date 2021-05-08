n=set(input().split())
t=int(input())
flag=1
for i in range(0,t):
    x=set(input().split())
    if(x.issubset(n)):
        flag=flag*1       
    else:
        flag=0
if flag==0:
    print("False")
else:
    print("True")
