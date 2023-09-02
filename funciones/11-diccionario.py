#diccionario es una coleccion de datos 

punto = { "x": 25, "y" : 50} # solo acepta string como llave
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
#print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25


for valor in punto:
    print(valor, punto[valor])

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Hela"},
    {"id": 2, "nombre": "Damian"},
    {"id": 3, "nombre": "Daniela"}
]
