from collections import deque
d=deque()
n=int(input())
for i in range(n):
    z=input()
    if z[0]=='a':
        z=z.split()
        if z[0]=='append':
            d.append(int(z[1]))
        elif z[0]=='appendleft':
            d.appendleft(int(z[1]))
    elif z=='pop':
        d.pop()
    elif z=='popleft':
        d.popleft()        
            
for i in d:
    print(i,end=' ')   