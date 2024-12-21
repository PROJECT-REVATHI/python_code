population=[
    ('banagalore',20000),
    ("chennai",300000),
    ("nellore",40000),
    ('amnhdra',5000000)
]

def filter_population(population):
    return population[1] > 200000

filtering = list(filter(filter_population,population))

print(filtering)






