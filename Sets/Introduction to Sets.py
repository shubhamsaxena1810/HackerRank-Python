def average(array):
    # your code goes here
    array=set(array)
    s=sum(array)
    l=len(array)
    return (float(s/l))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)