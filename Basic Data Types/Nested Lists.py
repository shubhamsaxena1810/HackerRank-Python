if __name__ == '__main__':
    final=list()
    for _ in range(int(input())):
        lst=list()
        name = input()
        score = float(input())
        lst.append(name)
        lst.append(score)
        final.append(lst)

final.sort(key = lambda x: x[1]) 

z=final[0][1]
for i in range (0,len(final)):
    if final[i][1]>z:
        z=final[i][1]
        break
    else:
        continue
final.sort(key = lambda x: x[0])
for i in range (0,len(final)):
    if final[i][1]==z:
        print(final[i][0])
