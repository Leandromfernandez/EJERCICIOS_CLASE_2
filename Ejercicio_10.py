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
contador_mujeres = 0
acumulador_notas_f = 0

nota_minima = None

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
    
    for nota in lista_notas:
        if nota_minima == None or nota < nota_minima:
            nota_minima = nota
            indice_menor_nota = contador
        
for i in range(len(lista_sexo)):   
        if lista_sexo[i] == "F":
            contador_mujeres += 1
            acumulador_notas_f += lista_notas[i]
promedio_notas_f = acumulador_notas_f / contador_mujeres       
 
print(f'la nota minima es: {nota_minima} y su nombre es: {lista_nombres[indice_menor_nota]}')
print(f'acumulador de notas f: {acumulador_notas_f}\n hay {contador_mujeres} mujeres\n el promedio de las notas es: {promedio_notas_f}')


