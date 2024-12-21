def first_two_chars(a,b):
    repalce1 = a[:2] + b[2:]
    replace2 = b[:2] + a[2:]
    return repalce1, replace2


a = 'hello'
b = 'world'
print(first_two_chars(a,b))
