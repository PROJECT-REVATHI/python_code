import re
s = 'make the world a *better place*'
pattern = r'\*(.*)\*'
replace = r'<b>\1<\\b>'
html = re.sub(pattern,replace,s)
print(html)