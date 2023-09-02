paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

def buscador(pais):
    for damian in paises:
        if pais == damian:
            return True
    return False

while True:
    print("\nIngresa el pais que quieres saber su capital: ")
    pais = input("")
    
    if buscador(pais) == True:
        print("\nLa capital de ",pais," es: ", paises[pais])
    else:
        print("no se a encontrado el Pais....")


    cc = input("Deseas hacer otra busqueda ? (preisone enter, o salir para terminar)")
    if cc == "salir":
        break

