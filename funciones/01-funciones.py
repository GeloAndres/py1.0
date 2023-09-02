def hola(nombre, apellido=" "): #La correcta definicion de "nombre" es parametro en este contexto
    print("Hola mundo")
    print(f"Ultimate Python {nombre} {apellido}") # aqui igual parametro


#El dato "Gelo" y "Daniela" se le denomina Argumento en este contexto
hola("Gelo", "Figueroa")
hola("Daniela", "Cataldo")
hola("Damian")


#Funcion con argumentos nombrados
hola(apellido="Figueroa",nombre="Damian")
