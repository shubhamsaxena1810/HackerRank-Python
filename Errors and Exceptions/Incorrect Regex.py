import re

t=int(input())
for i in range(t):
    z=input()
    try:
        re.compile(z)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)