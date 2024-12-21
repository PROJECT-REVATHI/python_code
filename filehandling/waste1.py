def read_last(fname,n):
    with open(fname,'r') as f1:
        file_read = f1.readlines()
        last_lines = file_read[-n:]
        for i in last_lines:
            print(i.strip())

name = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
n = 5
print(read_last(name,n))