def n_upper_chars(string):
    b=sum(map(str.isupper, string))
    if b>=2:
        return True
    else:
        return False
def n_num(string):
    b=sum(map(str.isdigit,string))
    if b>=3:
        return True
    else:
        return False

n=int(input())
for i in range(n):
    s=input()
    n1=len(list(s))
    n2=len(set(list(s)))
    if n1==n2 and n1==10 and s.isalnum() and n_upper_chars(s) and n_num(s):
        print('Valid')
    else:
        print('Invalid')