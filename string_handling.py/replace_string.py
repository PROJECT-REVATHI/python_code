def repalce(str):
    char =str[0]
    str = str.replace(char,'$')

    res = char + str[1:]


    return res

str = str(input("enter the string"))
print(repalce(str))

