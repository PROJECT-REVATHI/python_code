def read_n_lines(fname,n):
    with open(fname,'r') as f1:
        for i in range(n):
            line = f1.readline()
            if line:
                print(line.strip())
            else:
                break


filename = "C:\\Users\\Y.Rakesh Yadav\\OneDrive\\Desktop\\file1.txt"
num_lines = 2
read_n_lines(filename,num_lines)
