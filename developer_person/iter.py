for i in range(1,10):
    print(i)

my_iter = iter(range(1,11))
print(my_iter)
print(next(my_iter))

cars = iter(('audi', 'merzedes', 'wolvagen', 'bmw', 'porche', 'ferrari', 'ford'))

print(next(cars))
print(next(cars))
print(next(cars))
print(next(cars))
print(next(cars))
print(next(cars))
print(next(cars))
print(next(cars)) #no hay mas que iterar, por lo cual arroja error de iteracion
