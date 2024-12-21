import re
def check_string(string):
    pattern = re.compile('^\w+\S$')
    testcase = pattern.search(string)
    return testcase.group()


print(check_string('revathi'))