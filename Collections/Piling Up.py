t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]>a[len(a)-1]:
        b=a[0]
        a.remove(b)
    else:
        b=a.pop()
    ex=0
    while len(a)>1:        
        if a[0]>=a[len(a)-1] and a[0]<=b:
            b=a[0]
            a.remove(a[0])
        elif a[len(a)-1]>a[0] and a[len(a)-1]<=b:
            b=a.pop()
        else:
            ex=1
            print('No')
            break

    if ex==0 and a[0]<=b:
        print('Yes')