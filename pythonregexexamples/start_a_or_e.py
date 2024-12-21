import re
pattern = re.compile(r'\b(a\w+|e\w+)\b')
test  = 'aer erf ghy'
testcase = re.findall(pattern,test)
print(testcase)