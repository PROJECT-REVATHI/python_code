listing = [1,2,3,4,5,6,7,8,9,10]
print(listing)
evennum = list(filter(lambda x : x % 2 == 0,listing))
print(evennum)

oddnum = list(filter(lambda x : x % 2 != 0,listing))
print(oddnum)
