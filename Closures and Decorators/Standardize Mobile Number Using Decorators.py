def wrapper(f):
    def fun(l):
        # complete the function
        a=l
        l=[]
        for i in range(len(a)):
            l.append(a[i][-10:])
        l.sort()
        for i in l:
            print('+91 '+i[-10:-5]+' '+i[-5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 