names = ['revathi','suma','sridhar','appa','emun']
print(names)



def is_vowel(names):
    return names[0] in ['a','e','i','o','u']


filtering = list(filter(is_vowel,names))

print(filtering)