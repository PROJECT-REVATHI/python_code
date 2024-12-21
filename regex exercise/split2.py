import re
pattern = re.compile('[,!]')
test = pattern.search("revatghi is an software engineer")
m = pattern.split("revatghi is an software engineer")
print(test)
print(m)