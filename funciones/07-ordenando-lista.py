numeros = [2, 4, 1, 45, 71, 5, 3]

#numeros.sort(reverse = True)
numeros2 = sorted(numeros) #ordena la lista de menos a mayor
print(numeros)
print(numeros2)

usuario = [["Damián", 4], ["Daniela", 2], ["Gelo", 1]]

def ordena (elementos):
    return elementos[1]

usuario.sort(key=lambda el: el[1] , reverse=True)
print(usuario)
