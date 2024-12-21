def read_variable(fname):
    with open(fname,'r') as f1:
        reading_lines = f1.read()
    return reading_lines

fname = "C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
read_variable(fname)
