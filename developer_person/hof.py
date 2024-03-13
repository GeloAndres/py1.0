def increment(x):
    return x + 1

increment_v2 = lambda x: x +1

def high_ord(x, func):
    return x + func(x)

result = high_ord(2, increment)

#funcion dentro de otra funcion
#dos funciones separadas pero al momento de 
#llamarlas se llama una dentro de la otra

print(result)