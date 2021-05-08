a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def print_rangoli(size):
    for j in range(size):
        for i in range((size-(j+1))*2):
            print('-',end='')
        t=size
        for i in range(j+1):
            if i==j:
                print(a[t-1],end='')
                break
            else:
                print(a[t-1],end='-')
            t=t-1
        t=t-1
        for i in range(j):
            print('-',end='')
            t=t+1
            print(a[t],end='')
        
        for i in range((size-(j+1))*2):
            print('-',end='')
            
        print()
    for j in range(1,size):
        for i in range(j*2):
            print('-',end='')
        t=size-1
        for i in range(size-j):
            if i==size-j-1:
                print(a[t],end='')
                break
            else:
                print(a[t],end='-')
            t=t-1
        for i in range(size-1-j):
            print('-',end='')
            t=t+1
            print(a[t],end='')
        for i in range(j*2):
            print('-',end='')
        print()            
             
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    