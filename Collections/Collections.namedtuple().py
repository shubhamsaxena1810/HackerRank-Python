from collections import namedtuple
n=int(input())
a=input().strip().split()
Stud=namedtuple('Stud',a)
sum=0
for i in range(n):
    sum=sum+int(Stud(*input().split()).MARKS)
print(sum/n)
