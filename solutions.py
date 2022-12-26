"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def custom_max(n1:int, n2:int):
    """Dado dos argumentos de entrada retorna el maximo de ambos    

    Args:
        n1 (int): Primer num a comparar
        n2 (int): Segundo num a comparar
        
    Returns:
        int: Mayor de Ambos
    """
    
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    else:
        raise Exception("Los vaores no pueden ser iguales")
    raise Exception("Algo salio mal")
    


"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def custom_max_tres(n1:int,n2:int,n3:int):
    """Tres numeros y regresa la mayor de ellos

    Args:
        n1 (int): _description_
        n2 (int): _description_
        n3 (int): _description_
        
    Returns:
        int: Mayor de los tres
    """
    """
    a > b > c
    b > c
    a > c
    """
    n = custom_max(n1, n2)
    n_final = custom_max(n3, n)
    
    return n_final
print(custom_max_tres(1,5,2))

"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def vocal_id(letra):
    """Devolver si es vocal o no

    Args:
        letra (String): letra a considerar
    Returns: 
        String: Vocal o no
    """
    
    lista_vocals = ["a", "e", "i","o","u"]
    if letra in lista_vocals:
        print("Vocal")
        return True
    else:
        print("No vocal")
        return False 
    

"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
def inversa(cadena):
    """Arroja una cadena acomoda de forma inversa

    Args:
        cadena (String): cadena principal

    Returns:
        String: Cadena invertida
        
    forma facil
    
def invertir_cadena(cadena):
    return cadena[::-1]
    
    """
    cadena_inversa = ""
    for letra in cadena:
        cadena_inversa = letra + cadena_inversa
    return cadena_inversa


"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(cadena):
    """Devuelve un palindromo

    Args:
        cadena (String): cadena inicial
    Returns:
        String: Palindromo
    """
    
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        print("Es palindromo")
        return True


"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    """devuelve los iguales en una lista 

    Args:
        lista1 (list): _description_
        lista2 (list): _description_
    Returns:
        Boolean: True/False
    """
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True
    return False

print(superposicion([1,2,3],[5,6,2]))

"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres(caracter, n):
    string = caracter
    print(caracter * n)
    
print(generar_n_caracteres("xoxo", 4))