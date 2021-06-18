def user_check(u):
    a=['-','.','_']
    if u[0].isalpha():
        for i in u:
            if i.isalnum() or (i in a):
                continue
            else:
                return False
    else:
        return False
    return True

n=int(input())
for i in range(n):
    a=input()
    b=a.find('<')
    try:
        c=a[b+1:-1]
        c=c.split('@')
        u=c[0]
        c=c[1].split('.')
        d=c[0]
        c.remove(c[0])
        if len(c)>1:
            c=''.join(c)
            e=c
        else:
            e=c[0]
    except IndexError:
        continue
    if user_check(u) and d.isalpha() and (len(e)<=3 and e.isalpha()):
        print(a)