saludo="Hola Global" #no es buna practica ocupar variables globales


def saludar():
    saludo= "hola mundo"
    print(saludo)


def saludaGelo():
    saludo="Hola Gelo"
    print(saludo)


saludar()
saludaGelo()
saludar()

#no se deben opucar variables globales por malas practicas 
#y por razones practicas al momento de programar, ya que,
#se puede cambiar el valor en alguna funcion sin conocer su origen
#teniendo que buscar manualmente el pedazo de codigo que cambia tu valor.
