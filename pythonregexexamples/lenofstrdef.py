import re
pattern = re.finditer(r'([0-9]{1,3})','this is revathi a software engineer')
print("thsi is")
for n in pattern:
    print(n.group(0))