import re
def match_string(string):
    pattern = re.compile('\w*z.\w*')
    testcase = pattern.search(string)
    return testcase.group()
print(match_string('the lazy word lazy is lazy'))