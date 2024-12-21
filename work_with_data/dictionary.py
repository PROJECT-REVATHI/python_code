person_info = {
    'name':'revathi',
    # 1:'renuka',
    # ifg we have been used the
    # same key in the  immutable also
    # it will strike out the previous value an 
    # update the bnew value
    # 1:'suma',
    'age' : 10,
    'city':'nellore'

}

# print(person_info)
# print(type(person_info))
# print(person_info['name'])
# print(person_info.get('name'))
# print(person_info.get('age'))
# print(person_info.get(5,"default"))
# print(person_info.get(5))
# print(person_info.get(0))


# for k,v in person_info.items():
#     print("key is: %s" % k)
#     print("value is: %s" %v)
#     print("#########")

dict = {}
dict["city"] = "san francisco"
dict["name"] = "revathi"
print(dict)

dict1 = {"n":"revathi",
         "city":"nellore",
         "thing":"laptop"}


dict2 = {"n":"renuka",
         "city":"banglore",
         "thing":"mobile"}


dict1.update(dict2)
print(dict1)


TIM = {"najme":"revathi",
       "age":340,
       "city":"nellore"}
print(TIM)
del TIM["age"]
print(TIM)

# del keyword will be used to delete the key in an 
# dictionary if we are trying to del;ete the key that is non- existent the key will be deleted.
# we can also use the pop method to delete the information

print(TIM.pop("najme", None))
print(TIM)

# HAS_KEY METHOD WILL BE USED TO TEST IF THE KEY IS PRESENT OR NOT
alphabets = {1:'a'}
