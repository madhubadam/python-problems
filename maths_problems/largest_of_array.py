def big(li):
    m=li[0]
    for i in li:
        if i>m:
            m=i
    return m
a=big([34,34,23,45,333,564])
print(a)