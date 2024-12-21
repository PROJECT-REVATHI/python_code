student_data={
    'id1':{
        'name':'sara',
        'age':10,
        'subject':['english, math, science']
    },
    'id2':{
        'name':'revathi',
        'age':30,
        'subject':['english, math, science']
    },
    'id3':{
        'name':'sara',
        'age':10,
        'subject':['english, math, science']
        
    },
    'id4':{
        'name':'siri',
        'age':20,
        'subject':['english','math','science']
    }

}

# print(student_data.items())
# print(student_data.values())


updated_dict = {}
for key, value in student_data.items():
    print(key)
    print(value)
    if value not in updated_dict.values():
        updated_dict[key] = value


print(updated_dict)
        

