### Exception habdling  ###

numberOne, numberTwo = 5, 1
#print(5 + "5")
#print(numberOne + numberTwo)


#Un manejo de erorres para encapsularlo y controlarlo
try: 
    print(5 + 8)
    print("No se a producido un error")
except:
    print("Se a producido un error en el tipado. #error 203")
else:
    #se ejecuta si no hay una exceptcion
    print("La ejecucion coninua correctamente.")
finally:
    #se ejecuta simepre, pase lo que pase.
    print("La ejecucion esta en curso.....")

# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
except TypeError:
    #se ejecuta si se produce una excepecion
    print("Se ha producido un error.")
except ValueError as error:
    #se ejecuta si se produce una excepecion
    print("Se ha producido un error.")
    print(f"erro es {error}")


## captura de la informcion de las excepción

try:
    print(numberOne + "3")
except TypeError as typoError:
    print(f"Se a dectectado un error, es el siguiente: {typoError}")
except ValueError as error:
    #se ejecuta si se produce una excepecion
    print("Se ha producido un error.")
    print(f"El error es {error}")
except Exception as exceptionErrorcontrol:
    #error de variables en cualquier caso que se y ayuda a capturar error 
    print(f"Error, se a detectado el siguiente error.: {exceptionErrorcontrol}")
