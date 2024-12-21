from collections import Counter

dict1 = {
    'key1':10,
    'key2':20,
    'key3':30
}

dict2 = {
    'k1':10,
    'k2':20,
    'k3':30
}

concat = Counter(dict1) + Counter(dict2)
print(concat)
