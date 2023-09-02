def get_product(**datos): #este lleva dos astericos porque son kwargs
    print(datos["id"], datos["name"], datos["carg"])

get_product(id="0023",
            name="Gelo Figueroa",
            carg="Programador")
