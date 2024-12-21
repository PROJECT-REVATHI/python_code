def dividebyzero():
    try:
        a = int(input("enter the num"))
        b = int(input("enter the num"))
        c = a/b
        print(f"result:{c}")
    except ZeroDivisionError:
        print("zero is not divisible")

    finally:
        print("final block")

dividebyzero()
    