mydict = {
    'key1' :1,
    'key2' : 9,
    'key3' : 6,
    'key4' : 8

}

ascen = dict(sorted(mydict.items(),key = lambda item: item[1]))

print("ascen", ascen)