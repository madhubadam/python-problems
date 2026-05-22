def word(s):
    vowels='aeiouAEIOU'
    c=0
    for i in s:
     if i in vowels:
        c+=1
    return c
a=word("madhu")
print(a)
    