import re
pattern=re.compile('^\w+')
test_case = pattern.search('    789abcs')
print(test_case)





