if __name__ == '__main__':
    N = int(input())
    z=list()
    for i in range (0,N):
        name, *line = input().split()
        val = list(map(int, line))
        if name=="insert":
            z.insert(val[0],val[1])
        elif name=="print":
            print(z)
        elif name=="remove":
            z.remove(val[0])
        elif name=="append":
            z.append(val[0])
        elif name=="sort":
            z.sort()
        elif name=="pop":
            z.pop()
        elif name=="reverse":
            z.reverse()
