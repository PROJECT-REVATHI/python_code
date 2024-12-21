import re
def check_string(string):
    pattern = r'\d+'
    match = re.findall(pattern,string)
    print(match)
print(check_string('revathi 123 is 245 an software'))