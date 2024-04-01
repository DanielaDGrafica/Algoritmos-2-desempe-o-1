def suma_numeros_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma += numero
    return suma


lista_numeros = []


print("Ingrese los números uno por uno. Presione Enter sin ingresar nada para finalizar.")
while True:
    entrada = input("Número: ")
    if entrada == "":
        break  (alto)
    numero = int(entrada)
    lista_numeros.append(numero)

# Calcular la suma de los números pares
suma_pares = suma_numeros_pares(lista_numeros)

# Imprimir la suma de los números pares
print("La suma de los números pares es:", suma_pares)
