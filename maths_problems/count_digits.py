def num(n):
    c=0
    while n>0:
        n//=10
        c+=1
    return c
print(num(23456))