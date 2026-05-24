n=4
s=n*2-1
for i in range(s):
    for j in range(s):
        t=i
        l=j
        r=s-1-j
        b=s-1-i
        p=min(t,l,r,b)
        print(n-p,end=' ')
    print()
    
