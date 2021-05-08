s=list(str(input()))
i=0
while(i<=len(s)-1):
    count=1
    for j in range(i,len(s)-1):
        if(s[j]==s[j+1]):
            count+=1
        else:
            break
    print('(' +str(count) +', '+s[i] +')',end=' ')
    i=i+count
        