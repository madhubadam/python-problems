c=0
n=123434492992
while n>0:
    n=n//10
    c=c+1
    if n==0:
        break
print(c)