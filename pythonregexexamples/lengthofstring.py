import re
pattern = re.finditer(r"([0-9]{1,5})","revatgu u as an software enginer")
print("dinding the indexed in an string")
for n in pattern:
    print(n.group())
