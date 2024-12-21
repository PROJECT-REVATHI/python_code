import re
pattern = re.compile('.*[0-9]$')
testcase= pattern.search('aab')
print(testcase)