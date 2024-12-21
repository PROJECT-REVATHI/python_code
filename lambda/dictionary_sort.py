dictionary = [
    {'sam': 10},
    {'sam':5},
    {'sam':4},
    {'sam':3}
]

dic_sorting = dictionary.sort(key=lambda x:x['sam'])

print(dictionary)