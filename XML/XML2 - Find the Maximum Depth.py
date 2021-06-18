import xml.etree.ElementTree as etree

def depth(tree):
    lst = list(tree.iter());
    #print(len(lst));
    if len(lst) == 1:
        return 0;
    else:
        lst.remove(lst[0]);
        dpt = 0;
        for et in lst:
            #print(et);
            dpt = max(dpt, depth(et));
        return dpt + 1;
    
N = input();

count = 0;
xml = "";
for i in range(0, int(N)):
    xml += input();
tree = etree.ElementTree(etree.fromstring(xml));

print(depth(tree));