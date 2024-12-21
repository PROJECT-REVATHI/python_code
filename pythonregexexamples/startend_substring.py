import re
pattern = 'revathi'
text = 'revathi is an software engineer'
for m in re.finditer(pattern,text):
    s = m.start()
    e = m.end()
    print("match %s to %s"%(s,e))