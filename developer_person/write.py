name = input('Name: ')
last = input('Lastname: ')
age = input('Age: ')
estatura = input('Estatura: ')

with open('./developer_person/texto.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write(f'Nombre: {name} {last}, edad: {age}, Estatura: {estatura}\n')