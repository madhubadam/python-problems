import math
n=36
div=[]
for i in range(1,math.isqrt(n+1)):
    if n%i==0:
        div.append(i)
print(div)