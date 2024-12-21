import re
text = "revathi  "
pattern = re.sub("[  ,.]",":",text)
print(pattern)