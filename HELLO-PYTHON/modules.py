## modules ##

# modulos son como ocupar ficheros en este fichero 
# , en mejores terminos, es importar modulos (ficheros)
# para ser utilizados en este fichero.
import calucladora as cal

#sumo dos valores y los imprimo

pr = int(input("ingrese el primer numero: "))
se =  int(input("ingrese el segundo numero: "))
x = cal.sumar(pr, se)
y = cal.resta(pr, se)

print(f"Su suma es : {x} \nSu resta es: {y}")
