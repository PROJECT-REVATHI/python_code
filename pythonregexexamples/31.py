import re
text = 'revathi is , a , software engineer'
pattern = re.sub("[ ,.]",':',text)
print(pattern)