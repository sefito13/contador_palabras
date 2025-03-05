
signos = '.,:¿?;:"'

while True:
    texto = input("\nIngresa texto para realizar el conteo\n")
    texto = texto.lower()
    cantidad_palabras = {}

    #Elimina los signos
    for signo in signos:
        texto = texto.replace(signo, "")

    #Separa las palabras
    palabras = texto.split()

    #Hace el conteo de las palabras
    for palabra in palabras:
        cantidad_palabras[palabra] = cantidad_palabras.get(palabra, 0) + 1

    #Ordena las palabras de mayor a menor
    palabras_ordenadas = sorted(cantidad_palabras.items(), key=lambda x: x[1], reverse=True)

    #Identifica la palabra mas usada
    if palabras_ordenadas:
        max_usada, max_cantidad = palabras_ordenadas[0]
    else:
        max_usada, max_cantidad = "No hay palabras", 0

    #impresion de los resultados
    print(f"\n📊 Texto sin signos: {texto}")
    print(f"✅ Total de palabras: {len(palabras)}")
    print(f"\n📌 Frecuencia de palabras:")

    #enumera e imprime la cantidad de palabras
    for i, (palabra, cantidad) in enumerate(palabras_ordenadas[:3], start=1):
        print(f"{i}. '{palabra}' → {cantidad} veces")

    print(f"\n🔥 La palabra más usada es: '{max_usada}' con {max_cantidad} repeticiones.")


    seleccion = input("\nQuieres Realizar otro conteo? (s/n):").lower()
    if seleccion != 's':
        print("👋 ¡Gracias por jugar! Hasta la próxima. 😊")
        break

