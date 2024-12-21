def longest_word(words):
    longword = max(words,key=len)
    return longword



words = ['apple', 'banannana', 'summaaaa']
print(longest_word(words))