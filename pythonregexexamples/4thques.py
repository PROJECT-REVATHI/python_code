import re
pattern = re.compile('^a(b{2,3})$')
test_case = pattern.search('abv')
print(test_case)