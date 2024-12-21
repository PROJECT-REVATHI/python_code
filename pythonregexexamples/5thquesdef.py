import re
def check_string(string):
    pattern = re.compile('^[a-z]+_[a-z]+$')
    testcase = pattern.search(string)
    return testcase

print(check_string('abc_Dbc'))