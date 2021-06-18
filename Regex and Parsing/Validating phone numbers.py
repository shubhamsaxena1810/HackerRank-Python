def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
n=int(input())
for i in range(n):
    l=input()
    if (l[0]=='7' or l[0]=='8' or l[0]=='9') and len(l)==10 and is_num(l):
        print('YES')
    else:
        print('NO')