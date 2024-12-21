import re
pattern = 'revathi'
text = "the revathi is an softwre renuka"
match = re.search(pattern,text)
s = match.start()
e = match.end()
print("from %d to %d" %(s,e))
