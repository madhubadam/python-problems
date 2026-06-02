def factorial(num):
    fac=1
    while num>0:
         fac*=num
         num-=1
    return fac

num=int(input('enter the number:'))
print(factorial(num))
