def first_last(str):
    if len(str) < 2:
        return None
    else:
        res = str[0:2] + str[-2:]
        print(res)

str = str(input("enter string"))
print(first_last(str))