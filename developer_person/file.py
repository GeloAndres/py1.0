try:
    with open('./developer_person/texto.txt', 'r') as file:
        contenido = file.read()
        print(contenido)
        print('termio primera lectuera de texto')

except FileNotFoundError:
    print("El archivo 'texto.txt' no se encuentra en el directorio actual.")

# opcion2 
try:
    file2 = open('./developer_person/texto.txt')
    print(file2.read())
    print('termio segunda lectuera de texto')
except FileNotFoundError:
    print("El archivo2 'texto.txt' no se encuentra en el directorio actual.")

#opcion3 "linea por linea"
try:
    with open('./developer_person/texto.txt') as file:
        for line in file:
            print(line)

except FileNotFoundError:
    print("El archivo2 'texto.txt' no se encuentra en el directorio actual.")