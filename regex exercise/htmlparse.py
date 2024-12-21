import re
compile = re.compile('<.*?>')
m = compile.search('<html></html><div></div><div>')
print(m.group())
print(m.span())
