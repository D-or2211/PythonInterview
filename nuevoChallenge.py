def filtrar_palabras(lista, n):
    """filtrar palabras

    Args:
        lista (_type_): _description_
        n (_type_): _description_
    """
    palabrasFiltradas = []
    for palabra in lista:
        if len(palabra) > n:
            palabrasFiltradas.append(palabra)
    return palabrasFiltradas
array = ["hola","uno", "papanicolao", "sol", "Demian"]
palabras_filtradas = filtrar_palabras(array, 4)
#print(palabras_filtrada)

def detectorMayusculas():
    cadena = input("Ingresa una frase: ")
    for letra in cadena:
        if letra.isupper():
            print(letra)
detectorMayusculas()    