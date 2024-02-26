def suma (a , b):
    return(a + b)

print('tu resultado es: ', suma(3, 3))

def suma_rango(a, b):
    sum = 0
    for x in range(a,b):
        sum += x
    return sum


suma_rango(1,100)
suma_rango(10,100)
suma_rango(20,100000)
print(suma_rango(20,100000))

##funciones con retur, datos que devulve y no imprime desde la misma funcion

