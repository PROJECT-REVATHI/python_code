def extract(fname):

    list = []
    with open(fname,'r') as f1:
        read = f1.read()
        for line in read:
            if line.isalnum():
                list.append(line)



    return list


fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
data = extract(fname)
print("this is data %s" %(data))