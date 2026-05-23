n=5
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    for k in range(2*i):
        print(' ',end=' ')
    for l in range(n-i,0,-1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    for k in range(2*(n-i-1)):
        print(' ',end=' ')
    for l in range(i,-1,-1):
        print('*',end=' ')
    print()