def combine_file(f1,f2,f3):
    with open(f1,'r') as f1,open(f2,'r') as f2,open(f3,'w') as out:
        for line1, line2 in zip(f1, f2):
            out.write(line1.strip() + " "+line2.strip() + '\n')

    print(f"files have been successfully combines %s"%(f3))

f1 = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\f1.txt.txt"
f2 = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\f2.txt.txt"
f3 = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\f3.txt.txt"
combine_file(f1,f2,f3)
