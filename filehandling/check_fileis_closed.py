def check_file_close(fname):
    with open(fname,'r') as f1:
        before_close = f1.closed
    after_close = f1.closed
    return before_close, after_close


fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
before,after = check_file_close(fname)
print(f"file is closed before %s" %(before))
print(f"file is close after %s" %(after))




















