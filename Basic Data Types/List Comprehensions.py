x = int(input())
y = int(input())
z = int(input())
n = int(input())

a=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            b=[]
            if i+j+k!=n:
                b.append(i)
                b.append(j)
                b.append(k)
                a.append(b)
print(a)