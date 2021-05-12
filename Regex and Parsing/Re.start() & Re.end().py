import re
test = input()
q = input().strip()
y = re.finditer("(?=({}))".format(q), test)
z = []
for x in y:
    z.append((x.start(), x.start()+len(q) -1 )) #I realise that this is massively cheating.
if len(z) == 0:
    print((-1,-1))
else:
    for x in z:
        print(x)