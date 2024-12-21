
try:
    file1 = open(r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt","r")
    readc = file1.read()
    print(readc)
finally:
    file1.close()
