import re
pattern = re.compile('[a-z]+')
m = pattern.match('::: message')
p = pattern.search('::: message')
print(p.span())


# re.compiling-> compiling the string
# match - > strictkly starts with the start opf the string
# search - > search gfor whole string.