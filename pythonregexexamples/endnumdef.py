import re
def check_string(string):
    pattern = re.compile('.*[0-9]$')
    testcase = pattern.search(pattern)
    return testcase

print(check_string('ujijhg9'))