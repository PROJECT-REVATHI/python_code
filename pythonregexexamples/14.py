import re

pattern = re.compile('^[A-Za-z0-9_]*$')
test_case = pattern.search('The quick brown fox jumps over the lazy dog."')
print(test_case)
