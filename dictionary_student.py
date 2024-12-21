dict =[ {'name':'revathi','age':10,'grade': 110},
{'name':'suma','age':20,'grade': 100},
{'name':'sridhar','age':20,'grade': 95},
{'name':'sridhar','age':20,'grade': 87}]

def get_high_grade(s):
    return s['grade'] >= 95
highing = list(filter(get_high_grade,dict))
print(highing)

 