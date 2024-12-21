import re
pattern = re.compile('^[a-z]+_[a-z]+$')
test_case = pattern.search('abc_abc')
print(test_case)