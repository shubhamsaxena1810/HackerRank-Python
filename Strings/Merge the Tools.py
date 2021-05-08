def merge_the_tools(string, k):
    n=len(string)/k
    n=int(n)
    a=[]
    for i in range(n):
        a.append(string[i*k:(i+1)*k])
    for i in range(len(a)):
        c=""
        for j in range(len(a[i])):
            if a[i][j] in c:
                continue
            else:
                c=c+ a[i][j]
        print(c)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)