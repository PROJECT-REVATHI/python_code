import re
pattern = re.compile('^a.*?b$')
test_case = pattern.search('abbbbcg')
print(test_case)