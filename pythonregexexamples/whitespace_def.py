import re
def match_string(string):
    pattern = 'revathi is'
    match = pattern.replace(' ',string)
    return match

print(match_string('_'))