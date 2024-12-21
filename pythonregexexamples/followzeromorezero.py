import re
pattern = re.compile(r'^a(b*)$')
test_Case = pattern.search('abb')
print(test_Case)