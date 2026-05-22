n=5
for i in range(n):
    ascii=65
    for j in range(n-i):
        print(chr(ascii),end=' ')
        ascii+=1
    print()