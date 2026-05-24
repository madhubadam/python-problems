n=10
print('* '*n)
for i in range(1,n):
    for j in range(1):
        print('*',end=' ')
    for k in range(n-2):
        print(' ',end=' ')
    for l in range(1):
        print('*',end=' ')
    print()
print('* '*n)