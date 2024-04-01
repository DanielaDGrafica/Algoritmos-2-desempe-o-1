def ordenar_nombres():
    lista_nombres = []

    print("Ingrese los nombres uno por uno. Presione Enter sin ingresar nada para finalizar.")
    while True:
        nombre = input("Nombre: ")
        if nombre == "":
            break  # Terminar el bucle si el usuario no ingresa nada
        lista_nombres.append(nombre)

    lista_nombres.sort()

    print("Lista de nombres en orden alfabético:")
    for nombre in lista_nombres:
        print(nombre)

ordenar_nombres()
