def permission_exception(fname):
    try:
        with open(fname, 'w') as f1:
            read = f1.write("revathi")
            print(read)
    except PermissionError:
        print("permission error triggered")
    finally:
        print("fianl block")

file = str(input("enter the file name:"))
permission_exception(file)