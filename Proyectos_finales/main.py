## principal
import calculos as ca
import os

while True:
    os.system("cls")

    print("____________________________")
    print("Calculadora Gelo")
    print("")
    print("1.- suma")
    print("2.- resta")
    print("3.- multiplicacion")
    print("4.- divicion")
    print("5.- salir")
    print("")
    print("____________________________")
    print("")


    #datos de entradas
    op, x, y, resultado = int, int, int, int
    try:
        op = int(input("Ingresa la operacion: "))
        
        #salida
        if op == 5:
            break

        x = int(input("Ingresa el primer numero: "))
        y = int(input("Ingresa el segundo numero: "))        

    except Exception as error:
        print("Dato ingresado incorrecto....")
        print(f"El error fue: {error}")


#Separaciones logisticas.

    if op == 1:
        resultado = ca.suma(x, y)
        print(f"tu resultado es: {resultado}")
    elif op == 2:
        resultado = ca.resta(x, y)
        print(f"tu resultado es: {resultado}")
    elif op == 3:
        resultado = ca.multiplicacion(x, y)
        print(f"tu resultado es: {resultado}")
    elif op == 4:
        resultado = ca.divicion(x, y)
        print(f"tu resultado es: {resultado}")
    else:
        print("Esa operacion no se encuentra en nuestra calculadora.")
    
    input("pesione enter para continuar.....")
