def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

result = increment(15)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name es {name.title()} {last_name.title()}'


nombres = lambda name, nexName: f'sus dos nobres: {name.title()} {nexName.title()}'

print(nombres('gelo', 'andres'))

# las funciones tipo lambda se guardan detro de las variables como se ven ahi
#son super extra;as pero interesantes, cuales seran sus buenas practicas ??