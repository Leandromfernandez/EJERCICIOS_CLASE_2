""" Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5] """

contador = 0
lista_nombres = []
lista_sexo = []
lista_notas = []

while contador < 3:
    nombre = input('Ingrese un nombre: ')
    nombre = nombre.capitalize()    
    while nombre == "":
        nombre = input('Error. Ingrese un nombre: ')
        nombre = nombre.capitalize()
    
    sexo = input('Ingrese su sexo [M - F]: ')
    sexo = sexo.upper()
    while sexo != "M" and sexo != "F":
        sexo = input('Error. Ingrese su sexo [m - f]: ')
        sexo = sexo.upper()
    
    nota = int(input('Ingrese su nota: '))
    while nota <= 0 or nota > 10:
        nota = int(input('Error. Ingrese una nota valida: '))
        
    lista_nombres.append(nombre)
    lista_sexo.append(sexo)
    lista_notas.append(nota)
    
    contador += 1

print(f'el contador es: {contador}\ny la lista de nombres es {lista_nombres}\nsu sexo es: {lista_sexo}\ny su nota es: {lista_notas}')


