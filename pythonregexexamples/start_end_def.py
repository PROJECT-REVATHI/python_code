import re
def match_string(string):
    pattern = 'revathi'
    for m in re.finditer(pattern,string):
        s = m.span()
        return s
    
print(match_string('revathi is a software'))

