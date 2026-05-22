n=int(input())
rev=0
t=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if t==rev:
    print(f"{t} is palimdrone ")
else:
    print(f"{n} is not palimdrone")