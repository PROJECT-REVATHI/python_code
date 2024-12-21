import re
def check_string(string):
    pattern = re.compile('^a.*b$')
    test_case  = pattern.search(string)
    return test_case

print(check_string('abb6'))