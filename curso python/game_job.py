
#parte con funcioens
import random

def imprimir_encabezado(ronda):
    print('*' * 10)
    print(f'ROUND {ronda}')
    print('*' * 10)

def obtener_opcion_usuario():
    return input('piedra, papel o tijera => ').lower()

def imprimir_resultado(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        print('Empate!')
    elif (
        (opcion_usuario == 'piedra' and opcion_computadora == 'tijera') or
        (opcion_usuario == 'papel' and opcion_computadora == 'piedra') or
        (opcion_usuario == 'tijera' and opcion_computadora == 'papel')
    ):
        print(f'{opcion_usuario} gana a {opcion_computadora}')
        print('¡Usuario gana!')
        return 'user'
    else:
        print(f'{opcion_computadora} gana a {opcion_usuario}')
        print('¡Computadora gana!')
        return 'computer'

def jugar_juego():
    opciones = ('piedra', 'papel', 'tijera')
    victorias_computadora = 0
    victorias_usuario = 0
    ronda = 1

    while True:
        imprimir_encabezado(ronda)
        print('computer_wins', victorias_computadora)
        print('user_wins', victorias_usuario)

        opcion_usuario = obtener_opcion_usuario()
        ronda += 1

        if opcion_usuario not in opciones:
            print('Esa opción no es válida')
            continue

        opcion_computadora = random.choice(opciones)

        print('User option =>', opcion_usuario)
        print('Computer option =>', opcion_computadora)

        ganador = imprimir_resultado(opcion_usuario, opcion_computadora)

        if ganador == 'computer':
            victorias_computadora += 1
        elif ganador == 'user':
            victorias_usuario += 1

        if victorias_computadora == 2:
            print('El ganador es la computadora')
            break

        if victorias_usuario == 2:
            print('El ganador es el usuario')
            break

if __name__ == "__main__":
    jugar_juego()
