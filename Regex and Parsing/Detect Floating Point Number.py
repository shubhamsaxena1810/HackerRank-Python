def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
n=int(input())
for i in range(n):
    l=input()
    if l=='0':
        print("False")
        continue
    z=is_number(l)
    print(z)
