import re
s = '<html></html><head></head><title></title>'
length = len(s)
pattern = (re.match('<.*>',s).group())
print(pattern)
