L = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"}, 
    {"V": "S009"}, 
    {"VIII": "S007"}

]

print("original list", L)


unique = set(val for dict in L for val in dict.values())

print(unique)