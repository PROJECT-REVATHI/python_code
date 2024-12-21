import re
text = 'revathi 123 is a 414 revathi'
pattern = re.compile(r'\d+')
testcase = re.findall(pattern,text)
print(testcase)