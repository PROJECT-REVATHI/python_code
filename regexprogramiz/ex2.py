import re
pattern = re.compile('\s+')
replace = ''
string = 'abc 23 er gsjhfdfj 46'
m = re.sub(pattern,replace,string,1)
print(m)