n = int(input())
s = set(map(int, input().split()))
t=int(input())
for i in range(t):
    z=str(input())
    if z[0]=='p':
        s.pop()
    elif z[0]=='r':
        s.remove(int(z[-1]))
    elif z[0]=='d':
        s.discard(int(z[-1]))
print(sum(s))