import random
def random_file(fname):
    with open(fname, 'r') as f1:
        line = f1.readlines()
        random1 = random.choice(line)
        return random1.strip()



fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file1.txt" 
path = random_file(fname)
print("line %s" %(path))