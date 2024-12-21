import re

def match_string(string):
    pattern = re.compile('^[a-zA-Z0-9_]*$')
    test_case = pattern.search(string)
    return test_case.group()


print(match_string('Aa0_'))