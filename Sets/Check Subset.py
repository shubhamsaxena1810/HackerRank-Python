t = input()
for i in range(0,int(t)):
    z=input()
    x1=set(input().split())
    y=input()
    x2=set(input().split())
    flag = x1.issubset(x2)
    if flag==True:
        print("True")
    else:
        print("False")
   
