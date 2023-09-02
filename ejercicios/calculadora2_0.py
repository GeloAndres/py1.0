print("Hola buenas, aplicacion de calculadora.")
print("las operaciones de esta aplicacion son: suma, resta, div, multi")
print("")

#datos
resultado = 0

while True:

    n2 = 0
    op = ''

    # if resultado == 0:
    #     resultado = int(input('Ingrese el primer numero: '))
    
    # tambien se pudo a ver ocupado 'if not resultado', ya que, significa que si el valor que estamos verificando es igual a nulo, cero o nada 
    # lo toamra como verdadera la condicion para que entre al IF

    if not resultado:
        resultado = int(input('Ingrese el primer numero: '))

    op = input("Ingresa la operacion: ")

    #operacion de salida
    if op == 'salir':
        print("gracias por su preferecia.")
        break

    n2 = int(input("ingresa el segundo numero: "))

    #sala de operaciones
    if op == 'suma':
        #resultado = resultado + n2
        # se puede ocupar otra adignacion de operacion aqui como ejemplo +=
        resultado += n2
    elif op == 'resta':
        resultado = resultado - n2
    elif op== 'div':
        resultado = resultado / n2
    elif op == 'multi':
        resultado = resultado * n2 
    else:
        print('erro de los datos de entrada, favor ingrese denuevo.')

    print("")
    #print("el resultado de operacion: " ,resultado)
    #para mejorar mi codigo se implementara de otra manera el imprecion de texto en pantalla como a continuacion

    print(f"El resultado de operacion: {resultado}")
