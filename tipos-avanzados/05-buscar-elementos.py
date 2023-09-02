mascotas = ["hela","pelusa", "pulga", "felipe", "hela"]


print(mascotas.count("hela")) # para saber cuantas veces esta el mismo dato dentro de la misma lista
if "hela" in mascotas:
    print(mascotas.index("hela"))
else:
    print("No está.")
