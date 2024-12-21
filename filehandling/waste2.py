def read_last(fname,n):
    with open(fname,'r')as f1:
        read_content = f1.readlines()
        for i in read_content:
            if i:
                print(i.strip())
            else:
                break

fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
num = 2
read_last(fname,num)

       

            



