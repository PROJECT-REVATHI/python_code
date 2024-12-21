import re
def match_string(string):
    pattern = '\d+'
    test = re.findall(pattern, string)
    for a in test:
        print("found %s and %s" %(pattern,test))

print(match_string('revathi 124 is 789'))