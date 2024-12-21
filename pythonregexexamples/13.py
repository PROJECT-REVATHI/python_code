import re
pattern = re.compile('\Bz\B')
testcase = pattern.search('the lazy revathi is revathi lazy')
print(testcase.group())