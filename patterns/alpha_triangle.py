n=5
for i in range(1,n+1):
    ch=65+n-i
    for j in range(i):
        print(chr(ch+j),end=' ')
    print()