## Extrae los digitos
## ordenarlos de mayor a menor y devuelva en cadena
## sume todos los digitos y devuelva el resultado de la suma total
## todos los resultados deben ser al mismo tiempo

# Funciones logicas
def extraerDigitos(text):
    """
    Extrae los digitos de la cadena
    Args:
        text: String

    Returns: List

    """
    digitos = []
    for i in text:
        if i.isdigit():
            digitos.append(i)
    return digitos

def sortNmbers(digits):
    """
    Ordena de menor a mayor
    Args:
        digits: List
    Returns:
        sortedNmbers : List
    """
    sortedNmbers = sorted(digits)
    return sortedNmbers

def arrayConvert(sortedText):
    """
    Args:
        sortedText: List
    Returns:
        String: los numeros
    """
    str = ""
    for i in sortedText:
        str += i
    return str

def sumaString(lista):
    """
    Args:
        lista: List

    Returns:
        total: Int
    """
    total = 0
    for i in lista:
        total += int(i)
    return total

def showResults(digitos, mayorque, total):
    """
    Args:
        digitos:
        mayorque:
        total:

    Returns:
        String = finalString
    """
    msg = f'''
    Los digitos extraidos son: {digitos}
    Los digitos ordenados son: {mayorque}
    El total de la suma de estos es: {total}
'''
    return msg

if __name__ == "__main__":
    text = "3ha4sa2df3as5f3ad5a4sdf8df6"
    digitos = extraerDigitos(text)
    mayoramenor = sortNmbers(digitos)
    minuevaString = arrayConvert(mayoramenor)
    resultado = sumaString(mayoramenor)
    total = showResults(digitos, minuevaString, resultado)
    print(total)