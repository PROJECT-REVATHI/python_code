example = ['python','coding','purana']
starts_with = list(filter(lambda x:True if x[0] == 'p' else False,example))
print(starts_with)

# if it is only one value check
example = 'python'
starts_with = list(filter(lambda x:x == 'p',example))
print(starts_with)

# if it is true or false:
starts_with = lambda x: True if x.startswith('p') else False

print(starts_with('thon'))