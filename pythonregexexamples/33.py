import re
text  = 'quick brown the two'
pattern = re.findall(r"\b\w{5}\b",text)
print(pattern)