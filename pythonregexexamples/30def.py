import re
testcase = 'road is road'
pattern = re.sub(r'road', 'Rl',testcase)
print(pattern)