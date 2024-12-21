import re
def check_string(string):
    pattern = re.compile('^a(b+)$')
    check = pattern.search(string)
    return check.span()

print(check_string('ab'))