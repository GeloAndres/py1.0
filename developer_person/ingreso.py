#ingreso de datos de usuarios y guardado en archivos

nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
edad = input('Ingresa tu edad: ')
estatura = input('Ingresa tu estatura: ')

#integracion de los datos
try:
    with open('./developer_person/dato_cliente.txt', 'r+') as file:
        for line in file:
            print(line)
        file.write(f'Nombre: {nombre} {apellido}, edad: {edad}, Estatura: {estatura} \n')
except Exception as error:
    print('Se a producido un error inesperado.')