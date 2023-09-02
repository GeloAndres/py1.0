edad = 0

res = input("ingrese su edad: ")
edad = int(res)

if edad > 17 and edad < 50:
    print("puede ver la pelicula")
elif edad < 17 and edad > 0:
    print("Uste no puede ver la pelicula")
elif edad > 49:
    print("Uste puede ver la pelicula y extra, te regalamos un 40% de descuento")
else:
    print("Erro de ingreso de su edad o error de datos.")

print("Gracias por preferirnos.")

mensaje = "Esto es otro punto para poder ver la pelicula" if edad > 17 else "es menor"
print(mensaje)
