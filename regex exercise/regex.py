import re
pattern = '00'
s = '00000'
result = re.sub(pattern,'',s)
print(result)