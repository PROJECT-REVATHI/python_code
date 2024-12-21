import re
pattern = re.compile(r'(\W+)')
# m = pattern.split("revathi is an software engineer")
m = pattern.split('revathi is an sofrtware engineert',3)
print(m)