def store_list(fname):
    with open(fname,'r') as f:
        read = f.readlines()
    list = []

    for line in read:
        cleaned = line.strip()
        list.append(cleaned)
        
        
    return list


file  = "C:\\Users\\Y.Rakesh Yadav\\OneDrive\\Desktop\\file1.txt"
content = store_list(file)
print(content)