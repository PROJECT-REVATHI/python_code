import re

pattern = re.compile('[^a-zA-Z0-9$]')
test_case  = pattern.search('(bcs')
print("invalid" if test_case else "valid")