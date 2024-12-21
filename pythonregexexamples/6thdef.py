import re
def check_string(string):
    pattern = re.compile('^[A-Z+]+[a-z]+$')
    test_Case = pattern.search(string)
    return test_Case.group()

print(check_string('Abc'))