n1=0 
n2=1
nth=0
n=int(input())
for i in range(2,n+1):
    nth=n1+n2
    print(n1)
    n1=n2
    n2=nth
    if nth>=n:
        break
    