def last_lines(fname,n):
    with open(fname,'r') as f1:
        lines = f1.readlines()
        last_lines = lines[-n:]
        for line in last_lines:
            print(line.strip())

fname = "C:\\Users\\Y.Rakesh Yadav\\OneDrive\\Desktop\\file1.txt"
n = 3
last_lines(fname,n)