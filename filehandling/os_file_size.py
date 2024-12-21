import os
def get_path(fname):
    size = os.path.getsize(fname)
    print("path size %s" %(size))


fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
get_path(fname)