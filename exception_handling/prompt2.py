def valid_input(prompt):
    while True: 
        try:
            val = float(input(prompt))
            return val
        except ValueError:
            print("error")
        finally:
            print("this is finally block")



n1 = valid_input("enter the 1st number")
n2 = valid_input("enter the second number")
res = n1 * n2
