def remove_string(str,n):
    start = str[:n]
    end = str[n+1:]

    res = start + end
    print(res)




string_inp = str(input("enter the number"))
n = 3
print(remove_string(string_inp,n))
