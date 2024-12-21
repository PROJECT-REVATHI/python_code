def check_exception(string):
    try:
        value = int(input(string))
        return value
    except ValueError:
        print("invalid")


n = check_exception('please give input')
print("value",n)