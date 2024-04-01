def contar_vocales(frase):
    # Inicializar contadores para cada vocal
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    for letra in frase:
        # Convertir la letra a minúscula para comparar con las vocales
        letra = letra.lower()
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1
        elif letra == 'u':
            contador_u += 1

    print("Conteo de vocales:")
    print(f"Vocal 'a': {contador_a}")
    print(f"Vocal 'e': {contador_e}")
    print(f"Vocal 'i': {contador_i}")
    print(f"Vocal 'o': {contador_o}")
    print(f"Vocal 'u': {contador_u}")

entrada = input("Ingrese una palabra o frase para contar las vocales: ")

contar_vocales(entrada)
