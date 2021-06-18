v=['a','e','i','o','u','A','E','I','O','U']
l=input()
k=-1

for i in range(len(l)-2):
    m=''
    if (l[i] in v) and (l[i+1] in v):
        k=0
        for j in range(i,len(l)):
            z=l[j]
            if l[j] not in v:
                break
            else:
                m=m+l[j]
                k+=1
        if(m[len(m)-1]==z):
            break
        print(m)
        l=l[:i]+l[i+k:]
        i+=k
        if i>=len(l)-1:
            break
    else:
        continue
if k==-1:
    print(-1)