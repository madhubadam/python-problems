def reverse_func(s):
    rev=''
    for i in s:
        rev=i+rev
    return rev
a=reverse_func('madhu')
print(a)