from collections import Counter
def word_frequency(fname):
    with open(fname,'r') as f:
        content = f.read()

        words = content.split()

        # frequency
        freq = Counter(words)

    return freq

fname = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\file2.txt.txt"
word_freq = word_frequency(fname)
print(word_freq)

