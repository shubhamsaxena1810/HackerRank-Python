x,y=map(int,input().split())
for i in range(0,x//2):
    string=""
    for j in range (0,(2*i)+1):
        string=string+".|."
    print(string.center(y,'-'))

print("WELCOME".center(y,'-'))
z=x//2
while(z>0):
    string=""
    for j in range (0,(2*z)-1):
        string=string+".|."
    print(string.center(y,'-'))
    z=z-1
