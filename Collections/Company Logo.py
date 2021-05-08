d={}
a=1
s=list(input())
for i in range(len(s)):
    if s[i] in d:
        d[s[i]]+=a
    else:
        d[s[i]]=a
        
d = sorted(d.items(), key=lambda x: x[1], reverse=True)
i=(d[0][1])
c=[]
while(i>=1):
    b=[]
    for j in range(len(d)):
        if d[j][1]==i:
            b.append(d[j][0])
    b=sorted(b)
    c=c+b
    i=i-1

c=c[0:3]
for i in range(3):
    for j in range(len(d)):
        if c[i]==d[j][0]:
            print(c[i],d[j][1])