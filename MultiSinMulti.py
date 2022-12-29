## Crea un programa que multiplique sin utilizar el simbolo de multiplicacion

def multiplycacion(num1:int, num2:int):
    """
    multiplicacion sin usar *
    Args:
        num1: Int
        num2: Int
    Returns:
        resultado : Int
    """
    resultado = 0
    for repeticion in range(num2):
        resultado += num1
    return resultado

total = multiplycacion(10,2)
print(total)