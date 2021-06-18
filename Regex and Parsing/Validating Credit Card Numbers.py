n=int(input())
def start(a):
    if a[0]!='4' and a[0]!='5' and a[0]!='6':
        return False
    return True

def length(a):
    if a.find('-') !=-1:
        a=a.split('-')
        count=0
        for i in a:
            if len(i)!=4:
                return False
            else:
                count+=1
        if count>4:
            return False
        return True
    else:
        if len(a)!=16:
            return False
        else:
            return True
def check_4(a):
    for i in range(len(a)-5):
        if a[i]==a[i+1]==a[i+2]==a[i+3]:
            return False
    return True

for j in range(n):
    a=input()
    if start(a) and length(a):
        a = a.replace('-', "")
        if check_4(a) and a.isdigit():
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')