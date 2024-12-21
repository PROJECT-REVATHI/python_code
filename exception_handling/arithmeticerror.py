def arithmeticerror(n1,n2):
    try:
        res = n1/n2
        print(res)


    except ArithmeticError:
        print("arithmetice error")
    finally:
        print("finally block executes..")

n1= int(input("enter the number"))
n2 = int(input("enter the second number"))
result = arithmeticerror(n1,n2)
