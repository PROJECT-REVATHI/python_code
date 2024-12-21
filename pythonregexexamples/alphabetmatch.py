import re
pattern = re.compile('[^a-zA-Z0-9]')
regex = pattern.search('revathi006#')
print("invalid" if regex else "valid")