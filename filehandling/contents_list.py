def write_list(file_path, data_list):
    with open(file_path,'w') as f1:
        for item in data_list:
            f1.write(f"{item}\n")
    print(f"list content to path %s" %(file_path))


data_list  = ['revathi','suma','cherry','date','moon','sun']
filepath = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
write_list(filepath,data_list)



       


