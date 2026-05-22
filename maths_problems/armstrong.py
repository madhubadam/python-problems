n=int(input('enter the number:'))
c=0
t=n
a=n
total=0
while n>0:
    c+=1
    n//=10
while t>0:
    d=t%10
    total+=d**c
    t=t//10
if total==a:
    print(f"given number {a} is armstrong number")
else:
    print(f"given number {a} is not a armstrong number")
