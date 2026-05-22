n=5
for i in range(n):
    ascii=65+i
    for j in range(i+1):
        print(chr(ascii),end=' ')
        
    print()