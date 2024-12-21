import re

pattern = re.compile(r'(P\w+)\W(P\w+)')
text = "Python Panas pet"
testcase =re.findall(pattern,text)
print(testcase)