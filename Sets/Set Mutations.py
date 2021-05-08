x = int(input())
A = set(input().split())
n = int(input())
for i in range(0,n):
    z = input().split()
    if z[0]=="intersection_update":
        y=set(input().split())
        A.intersection_update(y)
    elif z[0]=="update":
        y=set(input().split())
        A.update(y)
    elif z[0]=="symmetric_difference_update":
        y=set(input().split())
        A.symmetric_difference_update(y)
    elif z[0]=="difference_update":
        y=set(input().split())
        A.difference_update(y)
sum=0
for i in A:
    sum=sum+int(i)
print(sum)
