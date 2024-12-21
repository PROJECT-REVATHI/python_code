import re
def match_string(string):
    pattern = re.sub('\.[0]*','.',string)
    # testcase= pattern.ma(string)
    return pattern
print(match_string('123.097.67.01'))