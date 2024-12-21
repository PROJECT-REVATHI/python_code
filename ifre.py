# import re
# pattern = re.compile('[a-z]+')
# m=pattern.match('revathi')
# print(pattern.match(':::message'))
# print(pattern.search(':::message'))
# print(m.group())


import re
pattern = re.compile(r'[a-z]+')
m = pattern.findall("revathi is an software")
print(m)
# if m:
#     print("match founded:", m.span())
# else:
#     print("match not founded")