import re
def check_string(string):
    pattern = re.compile('^a(b{3})$')
    testcase = pattern.search(string)
    return testcase

print(check_string('abv'))