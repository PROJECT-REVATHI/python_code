def exception(prompt):
    try:
        val = int(input(prompt))
        return val
    except ValueError:
        print("invalid")

n = exception("please give input")
print("input vaue", n)
