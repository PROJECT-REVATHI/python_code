# company = [["google", "facebook", "asmazon"],["revathi", "suma"]]
# print(company)

company = []
company.append("revathi")
company.append("facebook")
company.append("google")
company.insert(2,"cisco")

print(company)

lang = ["eng", "hin", "tamil"]
concat = company + lang
# print(concat)

lang.extend(company)
print(lang)
indexing = lang.index("hin")
print(lang.remove("eng"))
print(lang)
print(lang.pop())
print(lang.pop(0))
print(lang)

list = [1,6,9,8,4,2]
list.sort()
print(list)
list.reverse()
print(list)

# function over python list
comapnies = ["google", "facebook", "hackeearth"]
print(comapnies)

# for loop
for indx, name in enumerate(comapnies):
    print("index is %s for company: %s" %(indx,name))

listing = ["nanna","dioors", "love"]
print(listing)

print(sorted(listing))
print(listing)