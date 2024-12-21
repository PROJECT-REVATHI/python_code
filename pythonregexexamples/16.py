import re
ip = "216.08.094.196"
pattern = re.sub('\.[0]*','.',ip)
print(pattern)