def array(fname):
    with open(fname,'r') as f1:
        # read_content = f1.read()
        array = []
        
        for line in f1:
            clean = line.strip()
            array.append(clean)

    return array


fname = "C:\\Users\\Y.Rakesh Yadav\\OneDrive\\Desktop\\file1.txt"
store = array(fname)
print(store)

