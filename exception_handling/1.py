

def divide_number(x,y):
    try:
       result = x/y
       print("result:",result)
    except ZeroDivisionError:
        print("handle this error")

num = 10
den = 5
print(divide_number(num,den))
