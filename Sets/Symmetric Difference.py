def main():
    input()
    a = set(map(int,input().split()))
    input()
    b = set(map(int,input().split()))
    ans = a.difference(b)
    ans.update(b.difference(a))
    answer = list(ans)
    answer.sort()
    for num in answer:
        print(num)
                                                
main()