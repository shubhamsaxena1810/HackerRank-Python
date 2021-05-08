import math
degree_sign = u"\N{DEGREE SIGN}"
n1=int(input())
n2=int(input())
n3= pow(((n1*n1)+(n2*n2)),0.5)
z=round(math.degrees(math.asin(n1/n3)))
print(str(z)+degree_sign)