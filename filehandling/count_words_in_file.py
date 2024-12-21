def count_words(file):
    with open(file,'r') as f1:
        read = f1.read()
        strip = read.strip()
        length = len(strip)

    return length
       

fname= r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
word = count_words(fname)
print("length %s is %s" %(fname,word))
