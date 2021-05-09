x,k=map(int,input().split())
exp=str(input())
exp=exp.replace('x',str(x))
print(eval(exp)==k)