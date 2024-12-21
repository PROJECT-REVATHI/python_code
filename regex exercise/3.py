import re
pattern = re.compile(r'(\d{2})-(\d{4})')
test_string = pattern.findall('23-2321 55-99878 456-545 66-897677')
print(test_string)