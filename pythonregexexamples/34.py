import re
txt = 'rea reva revat'
pattern = re.findall(r'\b\w{3,5}\b',txt)
print(pattern)