def count_lines(fname):
    with open(fname,'r') as f1:
        line_count = sum(1 for line in f1)

    return line_count


fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt"
counting = count_lines(fname)
print(counting)
