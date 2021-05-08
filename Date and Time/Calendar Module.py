import calendar
m,d,y=input().split()
d=int(d)
m=int(m)
y=int(y)

n=(calendar.weekday(y,m,d))
days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[n])