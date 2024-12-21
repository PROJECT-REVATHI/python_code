import re
text ='revathi is an software in software company'
pattern = 'software'
for match in re.findall(pattern,text):
    print("%s" %match)