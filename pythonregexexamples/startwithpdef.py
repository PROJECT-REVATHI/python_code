import re
def check_string(string):
    pattern = r'(P\w+)\W(P\w+)'
    match = re.findall(pattern,string)
    return match
print(check_string('Print Pace'))