mydict = {
    'key1': 10,
    'key2': 20
}

check = 'key1'
# print(check)


if check in mydict:
    print(f"element found: %s" %check)
else:
    print("no element found")
    