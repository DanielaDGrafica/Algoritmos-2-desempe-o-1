def palabras_que_comienzan_con(letra, lista_palabras):
    palabras = []
    for palabra in lista_palabras:
        if palabra[0] == letra:
            palabras.append(palabra)
    return palabras


lista_palabras = []


print("Ingrese las palabras una por una. Presione Enter sin ingresar nada para finalizar.")
while True:
    palabra = input("Palabra: ")
    if palabra == "":
        break  (alto)
    lista_palabras.append(palabra)


letra = input("Ingrese la letra con la que deben comenzar las palabras: ")


print("Palabras que comienzan con la letra", letra + ":")
resultado = palabras_que_comienzan_con(letra, lista_palabras)
if resultado:
    for palabra in resultado:
        print(palabra)
else:
    print("No se encontraron palabras que comiencen con la letra", letra)

