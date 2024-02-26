import random

#dictionary comprehension
dict = {}
for i in range(1, 11):
    dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 11)}
print(dict_v2)

#mismo resultado, diferentes codigo


countries = ['col','mex','bol','per']

population = {}
for country in countries:
    population[country] = random.randint(1, 100)


countries_v2 = {country : random.randint(1,100) for country in countries}

print(population)

population_v2 = {country:random.randint(1,100) for country in countries}
print(countries_v2)

names = ['Gelo' , 'Daniela', 'Damian', 'Hela']
ages = [24, 20, 1, 1]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages )}