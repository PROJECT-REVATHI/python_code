import re
pattern = re.compile(r'a|b')
re = pattern.findall('cde ade acdbea')
print(re)