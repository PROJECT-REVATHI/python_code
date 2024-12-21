def append_file(fname,txt):
    with open(fname,'a') as f1:
        f1.write(txt + '\n')
    with open(fname, 'r') as f1:
        print("updated file content")
        print(f1.read())

fname = "C:\\Users\\Y.Rakesh Yadav\\OneDrive\\Desktop\\file1.txt"
txt = "appending the text"
append_file(fname,txt)
        