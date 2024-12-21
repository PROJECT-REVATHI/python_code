import re
text = 'reva is umaa'
pattern = re.findall(r'\b\w{4}\b',text)
print(pattern)