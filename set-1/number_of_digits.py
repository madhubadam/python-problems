def number_of_digits(num):
    #li=[]
    c=0
    while num>0:
        dig=num%10
        #li.append(dig)
        c+=1
        num//=10
    return c
num=int(input('enter the number'))
print(number_of_digits(num))
