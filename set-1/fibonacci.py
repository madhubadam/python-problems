def fibonacci(num):
    li=[]
    a,b=0,1
    while a<=num:
        li.append(a)
        a,b=b,a+b
    return li

num=49
print(fibonacci(num))
    