import re
pattern = re.compile(r'\d+')
test = 'revathi 567'
test_case = re.finditer(pattern,test)
for match in test_case:
    print("found %s in %s"%(match.start(),match.end()))