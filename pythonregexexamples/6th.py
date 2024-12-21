import re
pattern = re.compile('^[A-Z+]+[a-z]+$')
test_case = pattern.search('abc')
print(test_case)