from datetime import datetime
t=int(input())
for i in range(t):
    dt1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    dt2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    diff=max(dt1,dt2) - min(dt1,dt2)
    print(int(diff.total_seconds()))
