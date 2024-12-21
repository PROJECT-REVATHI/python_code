import re
pattern = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'revathi brungi')
m = pattern.groupdict()
print(m)
