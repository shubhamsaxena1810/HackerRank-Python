import re
r,c = map(int,input().split())
a=[]
for i in range(r):
    a.append(list(input()))
rez = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
b=''
for i in rez:
    b+=''.join(i)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b)) 