import re
pattern = re.compile('(yz|zy|zzy)')
m = pattern.findall('xyzy yz xyzx xzy zzy yz ')
print(m)