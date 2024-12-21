mydict = {
    'data1':1,
    'data2':2,
    'data3':3,
    'data4':4
}

res = 1

for item in mydict:
    res = res*mydict[item]

print(res)