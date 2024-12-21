def store_list(fname):
    with open(fname,'r') as f:
        lines = f.readlines()
    list = []

    for line in lines:
        lined = line.strip()
        list.append(lined)

    return list

file = "C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
filing= store_list(file)
print(filing)



        
    
