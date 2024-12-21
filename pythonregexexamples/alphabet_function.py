import re
def is_allowed(string):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    string = pattern.search(string)
    return not bool(string)

def check_string(string):
    pattern = re.compile(r'[a-zA-Z0-9]')
    return pattern.search(string)
    
res = check_string('abcd1230')
print(res)

