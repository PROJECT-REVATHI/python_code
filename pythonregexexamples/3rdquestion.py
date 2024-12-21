import re

pattern = re.compile('^ab?')
test = pattern.match('abbcd')
print(test)
