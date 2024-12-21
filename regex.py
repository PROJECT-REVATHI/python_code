import re
p = re.compile('[a-z]+')
m = p.match("suma")
print(m.start())
print(m.end())
print(m.span())
print(m.group())