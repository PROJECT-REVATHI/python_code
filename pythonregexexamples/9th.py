import re
pattern = re.compile('\w*z.\w*')
test_case = pattern.search('the quick revathi lazy is lazyness and lazyyness')
print(test_case.span())