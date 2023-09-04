""" Ejercicio 7:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares. """

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
lista_pares = []
for numero in lista_numeros:
    if numero % 2 == 0:
        numero_par = numero
        lista_pares.append(numero_par)

print(f'De la lista dada, los numeros pares son los siguientes: {lista_pares}')