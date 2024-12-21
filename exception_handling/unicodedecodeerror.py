def unicodedecodeerror(fname):
    try:
        with open(fname,'r',encoding='latin-1') as f1:
            read = f1.read()
            print(read)
    except unicodedecodeerror:
        print("unocdedecode eror")
    finally:
        print("finaly is execuetd")

fname= r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
unicodedecodeerror(fname)
