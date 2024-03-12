# veremos las funciones dentro de funciones o algo asi jajajaj

def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(11, increment)
print(result)

#creamos dos funcionse que la segunda llama a la primera pero de una manera peculiar

#creamos lo mismo pero en lambda
increment_v2 = lambda x : x + 1
high = lambda x, func: x + func(x)

result2 = high(11, increment_v2)
print(result2) 

#Geloncio