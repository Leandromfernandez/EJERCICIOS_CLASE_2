""" Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven """

edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]

edad_minima = None
indice_edad_minima = None

for i in range(len(edades)):
    if edad_minima == None or edades[i] < edad_minima:
        edad_minima = edades[i]
        indice_edad_minima = i

if indice_edad_minima is not None:
    nombre_mas_joven = nombre[indice_edad_minima]

print(f'La edad minima es {edad_minima} ,y es {nombre_mas_joven}')

