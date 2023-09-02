#crear una programa que detecte un palindromo y me arroje un TRUE O FALSE

#espacios en blancos
#reversa
def rever(dato):
    x = dato[::-1]
    return x


def pali(dato):
    nuevo_dato = ""
    for _ in dato:
        if _ != " ":
            nuevo_dato += _
    x = rever(nuevo_dato)
    if nuevo_dato.lower() == x.lower():
        return True
    elif nuevo_dato.lower() != x.lower():
        return False
    else:
        print("error de datos, ingrese nuevamente un dato correcto, gracias.")


print(pali("ooooooOOO   OO ooooo oo ooo o oo "))
