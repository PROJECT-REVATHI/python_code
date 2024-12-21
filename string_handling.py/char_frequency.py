def check_frequency(str):
    dict = {}
    for char in str:
        dict[char] = dict.get(char,0) + 1
    return dict

str = str(input("enter the string val"))
res = check_frequency(str)


for char,count in res.items():
    print(f"{count}: {char}")
