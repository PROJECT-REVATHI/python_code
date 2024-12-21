mixed_case_strings =[
    'Hello',
    'revathi',
    'suma',
    'raghav',
    'jayasree'
    
]

print(mixed_case_strings)
upper_case = list(filter(lambda x:x.isupper(), ''.join(mixed_case_strings)))

print(upper_case)