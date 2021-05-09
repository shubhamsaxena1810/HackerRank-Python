cube = lambda x: x*x*x

def fibonacci(n):
    a,b=0,1
    f=[]
    for i in range(n):
        f.append(a)
        c=b
        b=a+b
        a=c
    return (f)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))