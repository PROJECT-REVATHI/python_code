def filenofound(fname):
    try:
        with open(fname,'r') as f1:
            read = f1.read()
            print(read)
    except FileNotFoundError:
        print("file is not finding")
    finally:
        print("finally")


fname=  r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\fil1.txt"
f = filenofound(fname)
print(f)