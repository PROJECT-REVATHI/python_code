import re
def match_string(string):
    pattern = 'suma'
    for p in re.findall(pattern,string):
        return p


print(match_string('revathi is an software engineer'))