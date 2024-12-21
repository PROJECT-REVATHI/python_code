import re
def check_string(string):
    pattern = r'\b(a\w+|e\w+)\b'
    match = re.findall(pattern,string)
    return match

print(check_string('aer eru uir aer'))