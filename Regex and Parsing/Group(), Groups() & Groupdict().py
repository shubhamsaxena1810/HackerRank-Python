import re
s=str(input())
reg=re.compile(r'([a-zA-Z0-9])\1')
m=reg.search(s)
if m==None:
    print(-1)
else:
    print(m.group(1))