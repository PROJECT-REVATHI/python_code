def unknown(arg):
    return lambda n: arg * n


res = unknown(2)
print(res(15))

res = unknown(3)
print(res(3))


res = unknown(6)
print(res(2))


