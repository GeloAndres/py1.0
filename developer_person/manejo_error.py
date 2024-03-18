try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')


#divicion de errores
except ZeroDivisionError as error:
    print(error)

except AssertionError as error:
    print(error)

except Exception as error:
    print(error)


print('hola gente')

# importante
#cuando en mi bloque de codigo arriba tiene un error, sale del bloque ignorando todo lo escrito hacia abajo 
#para ir a la captacion del error en "except" y sigue adelante desde ahi mismo del programa