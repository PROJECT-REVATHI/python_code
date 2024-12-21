while True:
    try:
        user = int(input())
        print(user)
        if user < 0:
            raise ValueError("please give the positive integer")
        else:
            print("user input : %s" % user)
    except ValueError as e:
        print(e)
