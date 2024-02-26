import random
options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0
rounds = 1

def election():
    global rounds, computer_wins, user_wins

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1
    return user_option

while True:

    user_option = election() # que elije el pendejo
    
    if not user_option in options:
      print('esa opcion no es valida')
      continue

    computer_option = random.choice(options)

#--------------------------------------------------------#
    
import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
    print('*' * 10)
    print(f'ROUND {rounds}')
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('piedra, papel o tijera => ').lower()
    rounds += 1

    if user_option not in options:
        print('Esa opción no es válida')
        continue

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif (
        (user_option == 'piedra' and computer_option == 'tijera') or
        (user_option == 'papel' and computer_option == 'piedra') or
        (user_option == 'tijera' and computer_option == 'papel')
    ):
        print(f'{user_option} gana a {computer_option}')
        print('¡Usuario gana!')
        user_wins += 1
    else:
        print(f'{computer_option} gana a {user_option}')
        print('¡Computadora gana!')
        computer_wins += 1

    if computer_wins == 2:
        print('El ganador es la computadora')
        break

    if user_wins == 2:
        print('El ganador es el usuario')
        break
