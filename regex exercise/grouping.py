import re
pattern = re.compile('(xyz)x')
m = pattern.findall('xyz yz xyzx xyzx')
print([mat + 'x'for mat in m])