s=input()
upp=[]
low=[]
odd=[]
even=[]
for i in range(0,len(s)):
    if s[i].isupper():
        upp.append(s[i])
    if s[i].islower():
        low.append(s[i])
    if s[i].isdigit():
        if int(s[i])%2==0:
            even.append(s[i])    
        else:
            odd.append(s[i])

low.sort()
upp.sort()
even.sort()
odd.sort()
x=low+upp+odd+even
st=""
for i in range(0,len(x)):
    st=st+x[i]
print(st)