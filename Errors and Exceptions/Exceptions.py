t=int(input())
for i in range(t):
    a,b=input().split()
    try:
        a=int(a)
        b=int(b)
        print(a//b)
    except ZeroDivisionError as e1:
        print("Error Code:",e1)  
    except ValueError as e2:
        print("Error Code:",e2)