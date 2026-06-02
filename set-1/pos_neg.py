def pos_neg(num):
    if num==0:
        return 'number is zero'
    else:
        return 'postive'if num>0 else 'negative'

num=int(input('entre the number'))
print(pos_neg(num))