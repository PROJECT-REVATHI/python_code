import re

pattern = re.compile(r'^a')
testcase = pattern.search('ammu')
print(testcase)

def match_string(string):
    pattern = re.compile('a')
    testcase = pattern.search(string)
    return testcase.group()

print(match_string('ammun'))