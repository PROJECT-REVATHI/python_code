def str_replace(str):

    length = len(str)
    print(length)
    if length > 3:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'

    print(str)

    return str


str =str(input("enter the string"))
print(str_replace(str))