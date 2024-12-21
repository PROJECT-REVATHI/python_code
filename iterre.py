import re
pattern = re.compile(r'[a-zA-Z0-9]+')
# m = pattern.match("revatghiR1")
iterator = pattern.finditer('12 drmm dumm iiii')
for iter in iterator:
    print(iter.span())


print(re.match(r'[a-z]+','revarthi'))
