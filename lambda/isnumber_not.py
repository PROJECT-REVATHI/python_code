is_num = lambda q:q.replace('.','',1).isdigit()

# negative = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)
print(is_num('2345'))
print(is_num('-2345'))